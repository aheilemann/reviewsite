import React from "react";
import {Link} from "react-router-dom";

function Navbar() {
  return (
    <div>
      <Link to="/">Home </Link>
      {/* <Link to="/about">About Us </Link> */}
      <Link to="/signin">Signin </Link>
      <Link to="/signup">Signup </Link>
    </div>
  );
};

export default Navbar;
