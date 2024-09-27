import React from 'react';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <a href="/">AlbumRate</a>
      </div>
      <ul className="navbar-menu">
        <li><a href="/albums">Albumy</a></li>
        <li><a href="/reviews">Recenzje</a></li>
        <li><a href="/login">Zaloguj</a></li>
      </ul>
    </nav>
  );
};

export default Navbar;
