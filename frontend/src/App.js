import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
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

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Reviews</h1>
        {reviews.map((review) => <p>
          <a href={review.url}>{review.title}</a> (by: <a href={review.author_url}>{review.author}</a>) <br></br> {review.description}
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