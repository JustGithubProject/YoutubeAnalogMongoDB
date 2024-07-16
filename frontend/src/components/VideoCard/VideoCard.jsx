import React, { useState } from 'react';
import './VideoCard.css';
import axios from 'axios';
import { FaThumbsUp, FaEye } from 'react-icons/fa'; 

const VideoCard = ({ video }) => {
  const [likes, setLikes] = useState(video.likes);

  const pathToImage = `http://127.0.0.1:8080${video.preview_image_path}`;
  const videoUrl = `http://127.0.0.1:3000/watch?v=${video.video_path}`;

  const handleCardClick = async (event) => {
    event.preventDefault(); 
  
    try {
      const access_token = localStorage.getItem('access_token');
      await axios.post(`http://127.0.0.1:8000/video/video/view/${video._id}`)
      console.log('Successfully added');
      window.location.href = videoUrl;
    } catch (error) {
      console.error('Error increasing view count:', error);
    }
  };

  const handleLikeClick = async (event) => {
    event.preventDefault();
    event.stopPropagation();

    try {
      const access_token = localStorage.getItem('access_token');
      await axios.post(`http://127.0.0.1:8000/video/video/like/${video._id}`, {}, {
        headers: {
          Authorization: `Bearer ${access_token}`
        }
      });
      console.log('Successfully liked');
      setLikes(likes + 1);
    } catch (error) {
      console.error('Error increasing like count:', error);
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
          <button className="video-likes" onClick={handleLikeClick}>
            <FaThumbsUp /> {likes}
          </button>
        </div>
      </div>
    </a>
  );
};

export default VideoCard;
