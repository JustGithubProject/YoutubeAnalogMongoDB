import React from 'react';
import './Register.css';

const Register = ({ onToggle }) => {
  return (
    <div className="auth-container">
      <h2>Register</h2>
      <form>
        <div className="input-group">
          <label htmlFor="username">Username:</label>
          <input type="text" id="username" name="username" required />
        </div>
        <div className="input-group">
          <label htmlFor="email">Email:</label>
          <input type="email" id="email" name="email" required />
        </div>
        <div className="input-group">
          <label htmlFor="password">Password:</label>
          <input type="password" id="password" name="password" required />
        </div>
        <button type="submit" className="auth-button">Sign Up</button>
      </form>
      <button className="toggle-button" onClick={onToggle}>I already have an account</button>
    </div>
  );
};

export default Register;
