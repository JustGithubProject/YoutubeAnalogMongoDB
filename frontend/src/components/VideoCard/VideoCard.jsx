import React from 'react';
import './VideoCard.css'; 

const VideoCard = () => {
  return (
    <div className="video-card">
      {/* <img
        src="https://placeimg.com/300/100/any"
        alt="Sample Video"
        className="thumbnail"
      /> */}
      <div className="video-info">
        <h3 className="video-title">Sample Video Title</h3>
        <p className="channel">Channel Name</p>
        <p className="views">1,000,000 views</p>
      </div>
    </div>
  );
};

export default VideoCard;
