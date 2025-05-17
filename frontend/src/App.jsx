import { Routes, Route } from 'react-router-dom'
import Navbar from './components/NavBar';
import FileUpload from "./pages/FileUpload";
import HomePage from './pages/HomePage';

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        {/* <Route path="/navbar" element={<Navbar />} /> */}
        <Route path="/" element={<HomePage />} />
        <Route path="/upload" element={<FileUpload />} />
      </Routes>
    </div>
  );
}

export default App;