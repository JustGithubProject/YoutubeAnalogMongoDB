import React from 'react';
import Header from '../components/Header/Header';
import MainContent from '../components/MainContent/MainContent';
import "./Home.css"

const Home = () => {
    return (
        <div className="home-container">
            <Header/>
            <MainContent/>
        </div>
    )
}

export default Home;