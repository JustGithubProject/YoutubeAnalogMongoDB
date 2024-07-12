import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';

const SearchResult = () => {
    const [videos, setVideos] = useState([]);
    const location = useLocation();

    useEffect(() => {
        const params = new URLSearchParams(location.search);
        const title = params.get('title');

        if (title) {
            fetch(`http://127.0.0.1:8000/video/video/search/${title}`)
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
            <ul>
                {videos.map(video => (
                    <li key={video.id}>{video.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default SearchResult;
