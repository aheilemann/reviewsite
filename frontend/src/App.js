import React, { Component } from 'react';

class App extends Component {
  state = {
    reviews: [],
    currentuser: [],
  };

  async componentDidMount() {
    try {
      const res = await fetch('/api/reviews');
      const reviews = await res.json();
      this.setState({
        reviews
      });
    } catch (e) {
      console.log(e);
    }
    try {
      const res = await fetch('/api/currentuser');
      const currentuser = await res.json();
      this.setState({
        currentuser
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.reviews.map(review => (
          <div key={review.id}>
            <h1><a href={review.url}>{review.title}</a></h1>
            
            by: <a href={review.author_url}>{review.author}(id: {this.state.currentuser.id})</a> - Votes: {review.vote_score} <p></p> {review.description}
          </div>
        ))}
      </div>
    );
  }
}

export default App;
