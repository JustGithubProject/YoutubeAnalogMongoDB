import React, { useState, useEffect } from 'react';
import './Header.css';
import logo from "./images/new_logo.png";
import { ReactComponent as LogoutIcon } from './logout.svg'; 
import * as jwtDecodeModule from 'jwt-decode';
import { useNavigate } from 'react-router-dom';

const Header = () => {
    const navigate = useNavigate();
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [username, setUsername] = useState("");
    const [searchQuery, setSearchQuery] = useState("");

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
    };

    const handleSearchChange = (event) => {
        setSearchQuery(event.target.value);
    };

    const searchVideos = () => {
        window.location.href = `/results?title=${encodeURIComponent(searchQuery)}`;
    };

    return (
        <header className="header">
            <div className="logo">
                <a href="/">
                    <img src={logo} alt="Логотип" />
                </a>
            </div>
            <div className="search">
                <input 
                    type="text" 
                    placeholder="Search..." 
                    value={searchQuery} 
                    onChange={handleSearchChange} 
                    style={{ width: '400px' }} 
                />
                <button onClick={searchVideos}>
                    Search
                </button>
            </div>
            <nav className="nav">
                <ul>
                    {!isAuthenticated && (
                        <li><a href="/login">Sign in</a></li>
                    )}
                    {isAuthenticated && (
                        <>
                            <li><a href="/create/video">Создать видео</a></li>
                            <li>{username}</li>
                            <li>
                                <button onClick={logoutUser} className="logout-button">
                                    <LogoutIcon />
                                </button>
                            </li>
                        </>
                    )}
                </ul>
            </nav>
        </header>
    );
};

export default Header;
