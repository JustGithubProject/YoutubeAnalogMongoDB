import React, { useState, useEffect } from 'react';
import './Header.css';
import logo from "./images/new_logo.png";
import notification from "./images/notification.png"
import addVideo from "./images/ipad.png"
import profile from "./images/profile.png"
import { ReactComponent as SearchIcon } from './glass.svg';

const Header = () => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    useEffect(() => {
        // Проверяем наличие токена в localStorage
        const accessToken = localStorage.getItem('accessToken');
        if (accessToken) {
            setIsAuthenticated(true);
        } else {
            setIsAuthenticated(false);
        }
    }, []);

    return (
        <header className="header">
            <div className="logo">
                <a href="/">
                    <img src={logo} alt="Логотип" />
                </a>
            </div>
            <div className="search">
                <input type="text" placeholder="Search..." style={{ width: '400px' }} /> 
                <button><SearchIcon className="search-icon" /></button> 
            </div>
            <nav className="nav">
                <ul>
                    {!isAuthenticated && (
                        <>
                            <li><a href="/register">Sign up</a></li>
                            <li><a href="/login">Sign in</a></li>
                        </>
                    )}
                   {isAuthenticated && (
                    <>
                        <li><img src={notification} alt="notification"/></li>
                        <li><img src={addVideo} alt="addVideo"/></li>
                        <li><img src={profile} alt="Profile" /></li>
                    </>
                   )}
                    
                </ul>
            </nav>
        </header>
    );
};

export default Header;