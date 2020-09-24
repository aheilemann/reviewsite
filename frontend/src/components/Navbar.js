import React, { Component} from "react";
import { Link } from "react-router-dom";

import axiosInstance from "../axiosApi";


class Navbar extends Component {
    constructor(props) {
        super(props);
        this.state = {
            currentuser: [],
            // isLoggedIn: false,
          };
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
        this.getMessage("currentuser", "/user/current/");
    }

    async handleLogout() {
        try {
            const response = await axiosInstance.post('/blacklist/', {
                "refresh_token": localStorage.getItem("refresh_token")
            });
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            axiosInstance.defaults.headers['Authorization'] = null;
            return response;
        }
        catch (e) {
            console.log(e);
        }
    };
    render() {
        const isLoggedIn = this.state.currentuser.username;
        let navitems
        if (isLoggedIn) {
            navitems = 
                <nav>
                    <Link to={"/"}>Home</Link>
                    <Link to={"/hello/"}>Hello</Link>
                    <Link onClick={this.handleLogout}>Logout</Link>
                </nav>
            
        } else {
            navitems = 
                <nav>
                    <Link to={"/"}>Home</Link>
                    <Link to={"/login/"}>Login</Link>
                    <Link to={"/signup/"}>Signup</Link>
                </nav> 
        }
        return (
            <div>
                <Greeting isLoggedIn={isLoggedIn} />
                {navitems}
            </div>
        );
    };
};

function UserGreeting(props) {
    return <h1>Welcome back!</h1>;
}

function GuestGreeting(props) {
    return <h1>Please login or sign up.</h1>;
}
  
function Greeting(props) {
    const isLoggedIn = props.isLoggedIn;
    if (isLoggedIn) {
        return <UserGreeting />;
    }
    return <GuestGreeting />;
}

export default Navbar;
