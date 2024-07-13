import React from 'react';
import './Sidebar.css';

const Sidebar = () => {
  return (
    <div className="sidebar">
      <ul className="sidebar-menu">
        <li className="menu-item">
          <span><a href="/">Главная</a></span>
        </li>
        <li className="menu-item">
          <span>Библиотека</span>
        </li>
        <li className="menu-item">
          <span>История</span>
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;
