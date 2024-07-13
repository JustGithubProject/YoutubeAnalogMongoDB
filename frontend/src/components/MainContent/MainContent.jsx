import React, { useEffect, useState } from 'react';
import './MainContent.css';
import VideoCard from '../VideoCard/VideoCard';
import axios from 'axios';
import Sidebar from '../Sidebar/Sidebar';

const MainContent = () => {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    const fetchVideos = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/video/all-videos?limit=10');
        setVideos(response.data);
      } catch (error) {
        console.error("Error fetching videos:", error);
      }
    };

    fetchVideos();
  }, []);

  return (
    <div className="app-container">
      <Sidebar />
      <div className="main-content">
        <h1 className="title">Популярные видео</h1>
        <div className="video-row">
          {videos.map((video) => (
            <VideoCard key={video.id} video={video} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default MainContent;
