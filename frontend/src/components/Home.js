import React, { Component  } from 'react';
import Button from '@material-ui/core/Button';
import ButtonGroup from '@material-ui/core/ButtonGroup';
import './App.css';
import axiosInstance from "../axiosApi";

class Home extends Component {
  constructor() {
    super();
    this.state = {
      reviews: [],
      currentuser: [],
    }
  }
  

  async getMessage(key, path=key){
    try {
        let response = await axiosInstance.get(path);
        // const message = response.data;
        this.setState({
            [key]: response.data,
        });
        return response.data;
    }catch(error){
        console.log("Hello error: ", JSON.stringify(error, null, 4));
        // throw error; todo
    }
  }

  async componentDidMount() {
    this.getMessage('reviews');
    this.getMessage("currentuser", "/user/current/");
}

handleClick = (review, vote='up') => {
  
  axiosInstance.post('reviews/'+ review.id +'/vote/', {
    'action' : vote,
  })
}

  render() {
    const isLoggedIn = this.state.currentuser.username;
    
    return (
    <div className="App">
      <header className="App-header">
        {isLoggedIn} 
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
