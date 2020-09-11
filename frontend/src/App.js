import React, { Component  } from 'react';
// import './App.css';

class App extends Component {
  state = {
    reviews: [],
    currentuser: [],
  }

  async componentDidMount() {
    Promise.all([
      fetch('/api/reviews'),
      // fetch('/api/currentuser'),
      fetch('/api/users/current/')
    ])
    .then(([res1, res2]) => Promise.all([res1.json(), res2.json()]))
    .then(([data1, data2]) => this.setState({
      reviews: data1, 
      currentuser: data2
    }));
}

  handleClick = (review, vote='up') => {
    fetch('http://127.0.0.1:8000/api/reviews/'+ review.id +'/vote/', {
      method: 'POST',
      body: JSON.stringify({
        // user_id: this.currentuserid,
        'action' : this.vote,
      }),
      headers: {
        "Content-type": "application/json; charset=UTF-8",
        'Authorization': 'Basic ' + btoa('reviewuser:Hoxdo1-wetryt-ruqxuj'),
      }
    })
    // .then(response => response.json())
    // .then(json => console.log(json))
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          {this.state.reviews.map(review => (
            <div key={review.id}>
              <h1><a href={review.url}>{review.title}</a></h1>
              by: <a href={review.author_url}>{review.author}</a> - 
              Votes: {review.vote_score} 
              <button onClick={() => this.handleClick(review, this.vote='up')}>Upvote!</button>
              <button onClick={() => this.handleClick(review, this.vote='down')}>Downvote!</button>
              
              <p />{review.description}
            </div>
          ))}
        </header>
      </div>
    );
  }
}

export default App;
