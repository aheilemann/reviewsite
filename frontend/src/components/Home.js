import React, { Component  } from 'react';
import Button from '@material-ui/core/Button';
import ButtonGroup from '@material-ui/core/ButtonGroup';
import '../App.css';

class Home extends Component {
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
    const isLoggedIn = this.state.currentuser.username;

    return (
    <div className="App">
    <header className="App-header">
        <div>
        {this.state.currentuser.name} {isLoggedIn 
        ? <a href="http://127.0.0.1:8000/accounts/logout/">logout</a> 
        : <a href="http://127.0.0.1:8000/accounts/login/">login</a>}
        </div>
        {this.state.reviews.map(review => (
        <div key={review.id}>
            <h1>
            <ButtonGroup variant="text" color="primary" aria-label="text primary button group">
                <Button variant="contained" onClick={() => this.handleClick(review, this.vote='down')}>-</Button>
                <Button disabled variant="text" color="default">{review.vote_score}</Button>
                <Button variant="contained" onClick={() => this.handleClick(review, this.vote='up')}>+</Button>
            </ButtonGroup>
            <a href={review.url}>{review.title}</a>
            </h1>
            {review.description}
            <br /> by: <a href={review.author_url}>{review.author}</a>
        </div>
        ))}
    </header>
    </div>

    );
  }
}

export default Home;