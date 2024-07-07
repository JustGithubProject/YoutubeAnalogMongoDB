import React from 'react';
import './VideoCard.css'; 

const VideoCard = () => {
  return (
    <div className="video-card">
      <div className="video-info">
        <h3 className="video-title">Sample Video Title</h3>
        <p className="channel">Channel Name</p>
        <p className="views">1,000,000 views</p>
      </div>
    </div>
  );
};

export default VideoCard;
