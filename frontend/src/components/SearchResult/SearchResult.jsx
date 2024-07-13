import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import VideoCard from '../VideoCard/VideoCard';

const SearchResult = () => {
    const [videos, setVideos] = useState([]);
    const location = useLocation();

    useEffect(() => {
        const params = new URLSearchParams(location.search);
        const title = params.get('title');

        if (title) {
            fetch(`http://127.0.0.1:8000/video/video/search/?video_title_query=${title}`)
                .then(response => response.json())
                .then(data => {
                    setVideos(data);
                })
                .catch(error => {
                    console.error('Ошибка при загрузке видео:', error);
                });
        }
    }, [location]);

    return (
        <div>
            <h1>Результаты поиска</h1>
            <div className="video-results">
                {videos.map(video => (
                    <VideoCard key={video.id} video={video} /> 
                ))}
            </div>
        </div>
    );
};

export default SearchResult;
