import './App.css';
import Home from './pages/Home';
import AuthPage from './pages/AuthPage'
import AddVideoPage from "./pages/AddVideoPage"

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


function App() {
  return (
    <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<AuthPage/>} />
          <Route path="/create/video" element={<AddVideoPage/>} />
        </Routes>
    </Router>
  );
}

export default App;
