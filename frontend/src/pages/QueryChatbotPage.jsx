import React, { useState } from 'react';
import axios from 'axios';
import '../css/QueryChatbotPage.css'; // Import the CSS styles

export default function QueryChatbotPage() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await axios.post('http://127.0.0.1:8000/api/query/', { query });
      setResponse(res.data.answer);
    } catch (err) {
      setError('Error fetching data');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chatbot-container">
      <h1 className="chatbot-title">Document Research Chatbot</h1>

      <div className="chatbot-input-section">
        <input
          className="chatbot-input"
          placeholder="Ask your question..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button className="chatbot-button" onClick={handleSubmit} disabled={loading}>
          {loading ? 'Loading...' : 'Ask'}
        </button>
      </div>

      {error && <p className="chatbot-error">{error}</p>}

      {response && (
        <div className="chatbot-response-section">
          <div className="chatbot-card">
            <h2 className="chatbot-subtitle">Synthesized Answer</h2>
            <p>{response.synthesized_answer}</p>
          </div>

          <div className="chatbot-card">
            <h2 className="chatbot-subtitle">Citations</h2>
            {response.citations.map((citation, index) => (
              <div className="chatbot-citation" key={index}>
                <p><strong>Document ID:</strong> {citation["Document ID"]}</p>
                <p><strong>Extracted Answer:</strong> {citation["Extracted Answer"]}</p>
                <p><strong>Citation:</strong> {citation["Citation"]}</p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
