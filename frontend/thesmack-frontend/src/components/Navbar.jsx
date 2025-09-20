import "./Navbar.css";
import logo from "/src/assets/logo.png";

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <img src={logo} alt="The Slap Logo" />
      </div>
      <ul className="navbar-links">
        <li>
          <a href="#">Home</a>
        </li>
        <li>
          <a href="#">Profiles</a>
        </li>
        <li>
          <a href="#">Search</a>
        </li>
      </ul>
      <div className="navbar-search">
        <input type="text" placeholder="Search Here" />
        <button type="text">Go</button>
      </div>
    </nav>
  );
}

export default Navbar;
