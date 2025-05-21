
# 📄 API Documentation – `document_getter.py`

This module provides endpoints to retrieve and stream documents that were uploaded and parsed into the system.

---

## ✅ `/documents`

- **HTTP Method**: `GET`
- **Description**: Retrieves metadata of all documents that have been uploaded and stored in the MongoDB collection.
- **Parameters**: None

### 🔄 Response Format

Returns a list of JSON objects, each representing a document.

### 📤 Sample Output
```
[
  {
    "id": "682e35ef7bc3fae8d8caa639",
    "original_filename": "Wasserstoff Gen-AI Internship Task.pdf",
    "timestamp": "2025-05-22T01:52:07.665000",
    "file_path": "data\\docs\\Wasserstoff Gen-AI Internship Task_20250522_015205.pdf",
    "themes": [
      "AI Chatbot",
      "Document Analysis",
      "Theme Extraction",
      "Research Internship"
    ]
  }
]
```

- If a file is missing from the disk, the object will include an `error` key with a description.

---

## ✅ `/open`

- **HTTP Method**: `GET`
- **Description**: Opens and streams a file based on the provided path.
- **Parameters**:
  - `path: str` (query) — The normalized path to the file to be opened.

### 🔄 Response Format

- Returns the file as a `FileResponse` with the correct MIME type based on its extension (e.g., `application/pdf`, `image/png`).
- Returns HTTP `404 Not Found` if the file is missing on the disk.

---
