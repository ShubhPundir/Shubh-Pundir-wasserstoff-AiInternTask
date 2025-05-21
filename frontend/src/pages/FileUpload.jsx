import React, { useState } from "react";
import "../css/FileUpload.css"
import axios from "axios";

function FileUpload() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setMessage("");
  };

  const handleUpload = async () => {
    console.log("handleUpload() called")
    if (!file) {
      setMessage("Please select a file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/upload/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setMessage(`Success! Uploaded: ${response.data.filename}`);
    } catch (error) {
      setMessage(`Error: ${error.response?.data?.detail || "Upload failed"}`);
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Upload Document</h2>
      <input type="file" onChange={handleFileChange} accept=".pdf,.docx,.png,.jpg,.jpeg" />
      <button onClick={handleUpload} style={{ marginLeft: "1rem" }}>
        Upload
      </button>
      <p>{message}</p>
    </div>
  );
}

export default FileUpload;
