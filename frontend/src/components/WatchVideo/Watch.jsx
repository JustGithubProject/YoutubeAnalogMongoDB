import React from 'react';
import { useLocation } from 'react-router-dom';
import './Watch.css';

const Watch = () => {
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const videoPath = queryParams.get('v');
  const videoUrl = `http://127.0.0.1:8080${videoPath}`;

  return (
    <div className="watch-container">
      <div className="watch-video">
        <video width="800" controls>
          <source src={videoUrl} type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>
    </div>
  );
};

export default Watch;
