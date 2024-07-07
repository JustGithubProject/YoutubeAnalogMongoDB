import React from 'react';
import './Footer.css';

const Footer = () => {
    return (
        <footer className="footer">
            <div className="inner">
                <p align="center">&copy; 2024 Все права защищены</p>
                <div className="social-links">
                    <a href="https://facebook.com"><i className="fa fa-facebook"></i></a>
                    <a href="https://twitter.com"><i className="fa fa-twitter"></i></a>
                    <a href="https://instagram.com"><i className="fa fa-instagram"></i></a>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
