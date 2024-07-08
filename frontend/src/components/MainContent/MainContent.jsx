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
        setVideos(response.data); // Предполагая, что данные видео находятся в response.data
      } catch (error) {
        console.error("Error fetching videos:", error);
      }
    };

    fetchVideos();
  }, []);

  const chunkArray = (array, chunkSize) => {
    const chunks = [];
    for (let i = 0; i < array.length; i += chunkSize) {
      chunks.push(array.slice(i, i + chunkSize));
    }
    return chunks;
  };

  const videoChunks = chunkArray(videos, 3);

  return (
    <div className="main-content">
      {videoChunks.map((chunk, index) => (
        <div key={index} className="video-row">
          {chunk.map((video) => (
            <VideoCard key={video.id} video={video} />
          ))}
        </div>
      ))}
    </div>
  );
};

export default MainContent;
