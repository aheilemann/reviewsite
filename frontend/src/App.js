import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  function handleClick(e) {
    e.preventDefault();
    console.log('The link was clicked.');
  }

  // store reviews in a new variable
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    let fetchData = async () => {
      let response = await fetch('/api/reviews')
      let json = await response.json()
      setReviews(json)
    }
    fetchData()
  }, []);

  const [user, setUser] = useState([]);

  useEffect(() => {
    let fetchData = async () => {
      let response = await fetch('/api/users/current')
      let json = await response.json()
      setUser(json)
    }
    fetchData()
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Reviews</h1>
        {reviews.map((review) => <p>
          <button onClick={handleClick}>VoteUP</button>
          {user.username}
          <a href={review.url}>{review.title}</a> (by: <a href={review.author_url}>{review.author}</a> - Votes: {review.vote_score}) <br></br> {review.description}
        </p>
        )}
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;