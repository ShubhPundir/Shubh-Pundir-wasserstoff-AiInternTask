import React from 'react';
import { Link } from 'react-router-dom';
import '../css/HomePage.css'; // or './HomePage.css' depending on where you save it

function HomePage() {
  return (
    <div style={{ padding: '2rem', textAlign: 'center' }}>
      <h2>Welcome to Gen-AI Document Research Chatbot</h2>
      <p>This tool allows you to upload documents and ask questions about their content using AI.</p>
      <Link to="/upload">
        <button style={{ padding: '0.5rem 1rem', marginTop: '1rem' }}>
          Go to File Upload
        </button>
      </Link>
    </div>
  );
}

export default HomePage;
