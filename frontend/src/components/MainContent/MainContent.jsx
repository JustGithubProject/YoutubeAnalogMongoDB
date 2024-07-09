import React, { useEffect, useState, useRef } from 'react';
import './MainContent.css';
import VideoCard from '../VideoCard/VideoCard';
import axios from 'axios';

const MainContent = () => {
  const [videos, setVideos] = useState([]);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);
  const loaderRef = useRef(null);

  useEffect(() => {
    const fetchVideos = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/video/all-videos?page=${page}`);
        const newVideos = response.data.filter(video => !videos.some(existingVideo => existingVideo.id === video.id));
        setVideos((prevVideos) => [...prevVideos, ...newVideos]);
        if (response.data.length === 0) {
          setHasMore(false);
        }
      } catch (error) {
        console.error("Error fetching videos:", error);
      }
    };

    fetchVideos();
  }, [page]);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting && hasMore) {
          setPage((prevPage) => prevPage + 1);
        }
      },
      { threshold: 1.0 }
    );

    const currentLoaderRef = loaderRef.current;
    if (currentLoaderRef) {
      observer.observe(currentLoaderRef);
    }

    return () => {
      if (currentLoaderRef) {
        observer.unobserve(currentLoaderRef);
      }
    };
  }, [hasMore]);

  const chunkArray = (array, chunkSize) => {
    const chunks = [];
    for (let i = 0; i < array.length; i += chunkSize) {
      chunks.push(array.slice(i, i + chunkSize));
    }
    return chunks;
  };

  const videoChunks = chunkArray(videos, 3);

  return (
    <div className="main-content">
      {videoChunks.map((chunk, index) => (
        <div key={index} className="video-row">
          {chunk.map((video) => (
            <VideoCard key={video.id} video={video} />
          ))}
        </div>
      ))}
      {hasMore && <div ref={loaderRef} className="loader">Loading more videos...</div>}
    </div>
  );
};

export default MainContent;
