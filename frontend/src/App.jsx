import { Routes, Route } from 'react-router-dom'

import Navbar from './components/NavBar';
import FileUpload from "./pages/FileUpload";
import Home from './pages/Home';
import DocumentsPage from './pages/DocumentInterface';
import QueryChatbotPage from './pages/QueryChatbotPage';

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        {/* <Route path="/navbar" element={<Navbar />} /> */}
        <Route path="/" element={<Home />} />
        <Route path="/upload" element={<FileUpload />} />
        <Route path="/documents" element={<DocumentsPage />} />
        <Route path="/query" element={<QueryChatbotPage />} />
      </Routes>
    </div>
  );
}

export default App;