import React, { useState } from 'react';
import axios from 'axios';
import './AddVideo.css';

const AddVideoForm = () => {
  const [formData, setFormData] = useState({
    title: '',
    user_id: 'never mind backend can handle it',
    video_path: null,
    preview_image_path: null,
    description: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleFileChange = (e) => {
    setFormData({ ...formData, video_path: e.target.files[0] });
  };
  
  const handleFilePreviewImageChange = (e) => {
    setFormData({...formData, preview_image_path: e.target.files[0]})
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const accessToken = localStorage.getItem('access_token');

      if (!accessToken) {
        console.error('Отсутствует access_token в localStorage');
        return;
      }

      const formDataToSend = new FormData();
      formDataToSend.append('title', formData.title);
      formDataToSend.append('description', formData.description);
      formDataToSend.append('video_path', formData.video);
      formDataToSend.append("preview_image_path", formData.preview_image)

      const response = await axios.post('http://127.0.0.1:8000/video/video/add', formDataToSend, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
          'Content-Type': 'multipart/form-data',
        }
      });

      console.log('Response:', response.data);
      console.log('Видео успешно добавлено!');
      window.location.href = "/";
    } catch (error) {
      console.error('Ошибка при добавлении видео:', error);
    }
  };

  return (
    <form className="add-video-form" onSubmit={handleSubmit}>
      <label>
        Заголовок:
        <input
          type="text"
          name="title"
          value={formData.title}
          onChange={handleChange}
          required
        />
      </label>
      <label>
        Путь к видео:
        <input
          type="file"
          name="video_path"
          onChange={handleFileChange}
          required
        />
      </label>
      <label>
        Путь к preview image:
        <input
          type="file"
          name="preview_image_path"
          onChange={handleFilePreviewImageChange}
          required
        />
      </label>
      <label>
        Описание:
        <textarea
          name="description"
          value={formData.description}
          onChange={handleChange}
          required
        />
      </label>
      <button type="submit">Добавить видео</button>
    </form>
  );
};

export default AddVideoForm;
