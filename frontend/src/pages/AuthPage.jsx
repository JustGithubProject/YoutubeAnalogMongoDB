import React, { useState } from 'react';
import './Auth.css';
import Login from '../components/Login/Login';
import Register from '../components/Register/Register';

const AuthPage = () => {
  const [isLogin, setIsLogin] = useState(true);

  const handleToggle = () => {
    setIsLogin(!isLogin);
  };

  return (
    <div className="auth-page">
      {isLogin ? <Login onToggle={handleToggle} /> : <Register onToggle={handleToggle} />}
    </div>
  );
};

export default AuthPage;
