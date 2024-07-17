import React, { useState, useEffect } from 'react';
import './VideoCard.css';
import axios from 'axios';
import { FaThumbsUp, FaEye } from 'react-icons/fa';

const VideoCard = ({ video, currentUser }) => {
  const [likes, setLikes] = useState(video.likes);
  const [liked, setLiked] = useState(false);

  useEffect(() => {
    // Проверка, понравилось ли видео текущему пользователю
    if (currentUser && currentUser.liked.includes(video._id)) {
      setLiked(true);
    }
  }, [currentUser, video._id]);

  const pathToImage = `http://127.0.0.1:8080${video.preview_image_path}`;
  const videoUrl = `http://127.0.0.1:3000/watch?v=${video.video_path}`;

  const handleCardClick = async (event) => {
    event.preventDefault();
  
    try {
      const access_token = localStorage.getItem('access_token');
      await axios.post(`http://127.0.0.1:8000/video/video/view/${video._id}`, {}, {
        headers: {
          Authorization: `Bearer ${access_token}`,
        },
      });
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
      const url = liked
        ? `http://127.0.0.1:8000/video/video/put-away-like/${video._id}`
        : `http://127.0.0.1:8000/video/video/like/${video._id}`;

      await axios.post(url, {}, {
        headers: {
          Authorization: `Bearer ${access_token}`,
        },
      });

      setLiked(!liked);
      setLikes(liked ? likes - 1 : likes + 1);
      console.log(liked ? 'Successfully unliked' : 'Successfully liked');
    } catch (error) {
      console.error('Error updating like count:', error);
    }
  };

  return (
    <div className="video-card" onClick={handleCardClick}>
      <div className="video-thumbnail">
        <img src={pathToImage} alt="Preview" className="preview-image" />
      </div>
      <div className="video-info">
        <h3 className="video-title">{video.title}</h3>
        <p className="video-description">{video.description}</p>
        <div className="video-stats">
          <span className="video-views"><FaEye /> {video.views}</span>
          <button className="video-likes" onClick={handleLikeClick}>
            <FaThumbsUp style={{ color: liked ? 'blue' : 'black' }} /> {likes}
          </button>
        </div>
      </div>
    </div>
  );
};

export default VideoCard;
