import React from 'react';
import './Login.css';

const Login = ({ onToggle }) => {
  return (
    <div className="auth-container">
      <h2>Login</h2>
      <form>
        <div className="input-group">
          <label htmlFor="username">Username:</label>
          <input type="text" id="username" name="username" required />
        </div>
        <div className="input-group">
          <label htmlFor="password">Password:</label>
          <input type="password" id="password" name="password" required />
        </div>
        <button type="submit" className="auth-button">Sign in</button>
      </form>
      <button className="toggle-button" onClick={onToggle}>Create Account</button>
    </div>
  );
};

export default Login;
