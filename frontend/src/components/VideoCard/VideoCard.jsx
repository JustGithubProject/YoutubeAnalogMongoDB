import React from 'react';
import './VideoCard.css'; 

const VideoCard = ({video}) => {
  return (
    <div className="video-card">
      <div className="video-info">
        <h3 className="video-title">{video.title}</h3>
        <p className="description">{video.description}</p>
      </div>
    </div>
  );
};

export default VideoCard;
