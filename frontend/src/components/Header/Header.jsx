import React from 'react';
import './Header.css';
import logo from "./logo.png";

const Header = () => {
    return (
        <header className="header">
            <div className="logo">
                <img src={logo} alt="Логотип" />
            </div>
            <div className="search">
                <input type="text" placeholder="Поиск..." />
                <button>Найти</button>
            </div>
            <nav className="nav">
                <ul>
                    <li><a href="/">Главная</a></li>
                    <li><a href="/about">О нас</a></li>
                    <li><a href="/services">Услуги</a></li>
                    <li><a href="/contact">Контакты</a></li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;
