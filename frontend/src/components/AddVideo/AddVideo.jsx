import React, { useState } from 'react';
import axios from 'axios';
import './AddVideo.css'; 

const AddVideoForm = () => {
  const [formData, setFormData] = useState({
    title: '',
    user_id: 'never mind backend can handle it',
    video_path: '',
    description: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Получение access_token из localStorage
      const accessToken = localStorage.getItem('access_token');

      // Если access_token не найден, можно предпринять необходимые действия
      if (!accessToken) {
        console.error('Отсутствует access_token в localStorage');
        return;
      }

      // Отправка запроса с заголовком Authorization
      const response = await axios.post('http://127.0.0.1:8000/video/video/add', formData, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
          'Content-Type': 'application/json',
        }
      });

      console.log('Response:', response.data);
      // Дополнительная обработка успешного ответа здесь
      console.log('Видео успешно добавлено!');
      window.location.href = "/"
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
          type="text"
          name="video_path"
          value={formData.video_path}
          onChange={handleChange}
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
