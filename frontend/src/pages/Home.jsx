import { Link } from 'react-router-dom';
import '../css/Home.css';

function HomePage() {
  return (
    <div style={{ padding: '2rem', textAlign: 'center' }}>
      <h2>Welcome to Gen-AI Document Research Chat Query</h2>
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
