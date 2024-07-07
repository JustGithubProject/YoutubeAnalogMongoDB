import React from 'react';
import Header from '../components/Header/Header';
import MainContent from '../components/MainContent/MainContent';
import Footer from '../components/Footer/Footer';
const Home = () => {
    return (
        <div className="home-container">
            <Header/>
            <MainContent/>
            <Footer/>
        </div>
    )
}

export default Home;