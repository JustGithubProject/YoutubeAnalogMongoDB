import React, { useEffect, useState } from 'react';
import './MainContent.css';
import VideoCard from '../VideoCard/VideoCard';
import axios from 'axios';
import * as jwtDecodeModule from 'jwt-decode';

const MainContent = () => {
  const [videos, setVideos] = useState([]);
  const [currentUser, setCurrentUser] = useState(null);

  useEffect(() => {
    const fetchCurrentUser = async () => {
      try {
        const access_token = localStorage.getItem('access_token');
        if (access_token) {
          const decodedToken = jwtDecodeModule.jwtDecode(access_token);
          const username = decodedToken.username; 
          const response = await axios.get(`http://127.0.0.1:8000/users/user/${username}`, {
            headers: {
              Authorization: `Bearer ${access_token}`
            }
          });
          setCurrentUser(response.data);
        }
      } catch (error) {
        console.error("Error fetching current user:", error);
      }
    };

    const fetchVideos = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/video/all-videos?limit=10');
        setVideos(response.data);
      } catch (error) {
        console.error("Error fetching videos:", error);
      }
    };

    fetchCurrentUser();
    fetchVideos();
  }, []);

  return (
    <div className="app-container">
      <div className="main-content">
        <h1 className="title">Популярные видео</h1>
        <div className="video-row">
          {videos.map((video) => (
            <VideoCard key={video._id} video={video} currentUser={currentUser} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default MainContent;
