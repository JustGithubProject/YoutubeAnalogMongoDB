import React, { useState, useEffect } from 'react';
import './Header.css';
import logo from "./images/new_logo.png";
import notification from "./images/notification.png";
import addVideo from "./images/ipad.png";
import { ReactComponent as SearchIcon } from './glass.svg';
import { ReactComponent as LogoutIcon } from './logout.svg'; 
import * as jwtDecodeModule from 'jwt-decode';


const Header = () => {
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [username, setUsername] = useState("")

    useEffect(() => {
        const accessToken = localStorage.getItem('access_token');
        if (accessToken) {
            const decodedToken = jwtDecodeModule.jwtDecode(accessToken);
            setUsername(decodedToken.username);
            setIsAuthenticated(true);
        } else {
            setIsAuthenticated(false);
        }
    }, []);

    const logoutUser = () => {
        localStorage.removeItem("access_token");
        window.location.href = "/";
    }

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
                            <li><a href="/login">Sign in</a></li>
                        </>
                    )}
                    {isAuthenticated && (
                        <>
                            <li><img src={notification} alt="notification" /></li>
                            <li>
                                <img src={addVideo} alt="addVideo" />
                                <a href="/create/video">Создать видео</a>
                            </li>
                            <li>{username}</li>
                            <li><button onClick={logoutUser} className="logout-button"><LogoutIcon /></button></li>
                        </>
                    )}
                </ul>
            </nav>
        </header>
    );
};

export default Header;
