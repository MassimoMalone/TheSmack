import "./Navbar.css";
import logo from "/src/assets/logo.png";
import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <img src={logo} alt="The Slap Logo" />
      </div>
      <ul className="navbar-links">
        <li>
          <Link to="/" className="nav-link-item">
            Home
          </Link>
        </li>
        <li>
          <Link to="/profile" className="nav-link-item">
            profile
          </Link>
        </li>
        <li>
          <Link to="/login" className="nav-link-item">
            login
          </Link>
        </li>
      </ul>
      <div className="navbar-search">
        <input type="text" placeholder="Search Here" />
        <button type="button">Go</button>
      </div>
    </nav>
  );
}

export default Navbar;
