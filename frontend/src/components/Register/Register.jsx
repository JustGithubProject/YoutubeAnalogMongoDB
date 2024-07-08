import React, { useState } from 'react';
import './Register.css';
import axios from 'axios';

const Register = ({ onToggle }) => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleRegister = async (e) => {
    e.preventDefault(); // Предотвращаем стандартное поведение формы
    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/auth/register',
        {
          username: username,
          email: email,
          password: password,
        },
        {
          withCredentials: true,
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );
      console.log("Register successful", response.data);
      window.location.href = "/login";
    } catch (error) {
      if (error.response) {
        console.log("Register failed", error.response.data);
      } else {
        console.log("Register failed", error.message);
      }
    }
  };

  return (
    <div className="auth-container">
      <h2>Register</h2>
      <form onSubmit={handleRegister}>
        <div className="input-group">
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            name="username"
            onChange={(e) => setUsername(e.target.value)}
            value={username}
            required
          />
        </div>
        <div className="input-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            onChange={(e) => setEmail(e.target.value)}
            value={email}
            required
          />
        </div>
        <div className="input-group">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            onChange={(e) => setPassword(e.target.value)}
            value={password}
            required
          />
        </div>
        <button type="submit" className="auth-button">Sign Up</button>
      </form>
      <button className="toggle-button" onClick={onToggle}>I already have an account</button>
    </div>
  );
};

export default Register;
