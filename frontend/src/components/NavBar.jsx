import { Link } from "react-router-dom";
import "../css/NavBar.css";  // Optional for styling

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to='/' style={{ textDecoration: 'none', color: 'inherit' }}>
          Gen-AI Chat Query
        </Link>
      </div>
      <ul className="navbar-links">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/upload">Upload</Link></li>
        <li><Link to="/documents">Documents</Link></li>
        <li><Link to="/query">Query</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
