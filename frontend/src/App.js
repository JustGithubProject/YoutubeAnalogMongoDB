import './App.css';
import Home from './pages/Home';
import AuthPage from './pages/AuthPage'

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


function App() {
  return (
    <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<AuthPage/>} />
        </Routes>
    </Router>
  );
}

export default App;
