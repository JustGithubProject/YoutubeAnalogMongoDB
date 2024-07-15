import React from 'react';
import './VideoCard.css';
import axios from 'axios';
import { FaThumbsUp, FaEye } from 'react-icons/fa'; 

const VideoCard = ({ video }) => {
  const pathToImage = `http://127.0.0.1:8080${video.preview_image_path}`;
  const videoUrl = `http://127.0.0.1:3000/watch?v=${video.video_path}`;

  const handleCardClick = async (event) => {
    event.preventDefault(); 
  
    try {
      const access_token = localStorage.getItem('access_token');
      await axios.post(
        `http://127.0.0.1:8000/video/video/view/${video._id}`,
        {},
        {
          headers: {
            Authorization: `Bearer ${access_token}`,
          },
        }
      );
      console.log('Successfully added');
      window.location.href = videoUrl;
    } catch (error) {
      console.error('Error increasing view count:', error);
    }
  };

  return (
    <a href={videoUrl} className="video-card" onClick={handleCardClick}>
      <div className="video-thumbnail">
        <img src={pathToImage} alt="Preview" className="preview-image" />
      </div>
      <div className="video-info">
        <h3 className="video-title">{video.title}</h3>
        <p className="video-description">{video.description}</p>
        <div className="video-stats">
          <span className="video-views"><FaEye /> {video.views}</span>
          <span className="video-likes"><FaThumbsUp /> {video.likes}</span>
        </div>
      </div>
    </a>
  );
};

export default VideoCard;
