import React, { Component} from "react";
import { Switch, Route } from "react-router-dom";
import Home from "./home";
import Login from "./login";
import Signup from "./signup";
import Hello from "./hello";
import Navbar from "./navbar";

class App extends Component {


    render() {
        return (
            <div className="site">
                <Navbar />
                <main>
                    <Switch>
                        <Route exact path={"/login/"} component={Login}/>
                        <Route exact path={"/signup/"} component={Signup}/>
                        <Route exact path={"/hello/"} component={Hello}/>
                        <Route path={"/"} component={Home}/>
                    </Switch>
                </main>
            </div>
        );
    }
}

export default App;
