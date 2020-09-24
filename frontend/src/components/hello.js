import React, { Component } from "react";
import axiosInstance from "../axiosApi";


class Hello extends Component {
    constructor() {
        super();
        this.state = {
          message: '',
          currentuser: [],
        }
      }
    
      async getMessage(){
        try {
            let response = await axiosInstance.get('/hello/');
            const message = response.data.hello;
            this.setState({
                message: message,
            });
            return message;
        }catch(error){
            console.log("Hello error: ", JSON.stringify(error, null, 4));
            // throw error; todo
        }
      }    
      async getCurrentuser(){
        try {
            let response = await axiosInstance.get('currentuser');
            const message = response.data.username;
            this.setState({
                currentuser: message,
            });
            return response.data;
        }catch(error){
            console.log("Hello error: ", JSON.stringify(error, null, 4));
            // throw error; todo
        }
      }

    async componentDidMount() {
        this.getMessage();
        this.getCurrentuser();
    }

    render(){
        return (
            <div>
                <p>{this.state.currentuser} {this.state.message}</p>
            </div>
        )
    }
}

export default Hello;
