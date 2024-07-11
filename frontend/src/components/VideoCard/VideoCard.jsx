import React from 'react';
import './VideoCard.css'; 

const VideoCard = ({video}) => {
  console.log(video.preview_image_path)
  const pathToImage = `http://127.0.0.1:8080${video.preview_image_path}`;
  return (
    <div className="video-card">
      <div className="video-info">
        <h3 className="video-title">{video.title}</h3>
        <p className="description">{video.description}</p>
        <img src={pathToImage} alt="Preview" className="preview-image" />
      </div>
    </div>
  );
};

export default VideoCard;
