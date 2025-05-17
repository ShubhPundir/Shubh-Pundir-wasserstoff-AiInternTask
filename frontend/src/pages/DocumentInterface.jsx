import { useEffect, useState } from 'react';
import '../css/DocumentInterface.css';

const DocumentsPage = () => {
  const [documents, setDocuments] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/documents')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch documents');
        }
        return response.json();
      })
      .then((data) => {
        setDocuments(data);
      })
      .catch((err) => {
        setError(err.message);
      });
  }, []);

  const convertToURL = (filePath) => {
    return `http://127.0.0.1:8000/api/open?path=${encodeURIComponent(filePath)}`;
  };

  const formatTimestamp = (ts) => {
    if (!ts) return '-';
    const date = new Date(ts);
    return date.toLocaleString();
  };

  return (
    <div className="documents-container">
      <h1 className="documents-title">Available Documents</h1>

      {error && <p className="error-message">Error: {error}</p>}

      <div className="table-wrapper">
        <table className="documents-table">
          <thead>
            <tr>
              <th>S.No.</th>
              <th>Original Filename</th>
              <th>Timestamp</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            {documents.length === 0 ? (
              <tr>
                <td colSpan="4" className="no-documents">
                  No documents found.
                </td>
              </tr>
            ) : (
              documents.map((doc, index) => (
                <tr key={doc.id}>
                  <td>{index + 1}</td>
                  <td>{doc.original_filename}</td>
                  <td>{formatTimestamp(doc.timestamp)}</td>
                  <td>
                    {doc.file_path ? (
                      <a
                        href={convertToURL(doc.file_path)}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="link-open-file"
                      >
                        Open File
                      </a>
                    ) : (
                      <span className="error-text">{doc.error || 'Unavailable'}</span>
                    )}
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default DocumentsPage;
