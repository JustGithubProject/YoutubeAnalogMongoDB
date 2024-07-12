import React from 'react';
import './VideoCard.css';

const VideoCard = ({ video }) => {
  const pathToImage = `http://127.0.0.1:8080${video.preview_image_path}`;
  const videoUrl = `http://127.0.0.1:3000/watch?v=${video.video_path}`;

  return (
    <a href={videoUrl} className="video-card">
      <div className="video-thumbnail">
        <img src={pathToImage} alt="Preview" className="preview-image" />
      </div>
      <div className="video-info">
        <h3 className="video-title">{video.title}</h3>
        <p className="video-description">{video.description}</p>
      </div>
    </a>
  );
};

export default VideoCard;
