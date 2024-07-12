import React, { useEffect, useState } from 'react';
import './MainContent.css';
import VideoCard from '../VideoCard/VideoCard';
import axios from 'axios';

const MainContent = () => {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    const fetchVideos = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/video/all-videos');
        setVideos(response.data);
      } catch (error) {
        console.error("Error fetching videos:", error);
      }
    };

    fetchVideos();
  }, []);

  return (
    <div className="main-content">
      <div className="video-row">
        {videos.map((video) => (
          <VideoCard key={video.id} video={video} />
        ))}
      </div>
    </div>
  );
};

export default MainContent;
