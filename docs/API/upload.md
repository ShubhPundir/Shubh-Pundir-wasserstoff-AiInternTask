# 📄 API Documentation – `upload.py`

This module provides an endpoint to upload documents (PDF, DOCX, images), parse their content, extract themes, store parsed data in MongoDB, and ingest embeddings into a vector store (Qdrant).

---

## ✅ `/upload/`

- **HTTP Method**: `POST`
- **Description**: Uploads a single file, validates its type, saves it on disk, parses the document into text pages, extracts themes from the text, stores metadata and parsed text in MongoDB, and ingests the parsed content into a vector store for semantic search.
- **Parameters**:
  - `file` (form-data) — The file to upload. Supported types are `.pdf`, `.docx`, `.png`, `.jpg`, `.jpeg`.

### 🔄 Workflow Details

1. Validates the file extension against allowed types.
2. Saves the uploaded file in `data/docs/` with a unique timestamped filename.
3. Parses the document into pages of text using `parse_document`.
4. Flattens extracted text and extracts themes via `extract_themes_from_document`.
5. Stores document metadata, parsed text, and extracted themes in MongoDB collection `parsed_docs`.
6. Ingests the parsed pages into the Qdrant vector store with `ingest_to_qdrant`.
7. Handles errors with appropriate HTTP status codes and messages.

### 📤 Sample Request

```bash
curl -X POST "http://yourapi/upload/" -F "file=@/path/to/document.pdf"
```

### 📤 Sample Output
```
{
  "message": "File uploaded, parsed, and stored successfully",
  "filename": "document_20250522_012345.pdf",
  "document_id": "60a7f7bfa98c4b6d883f3c7a"
}

```
### ❗ Error Responses
400 Bad Request: Unsupported file extension.

500 Internal Server Error: Parsing failure, MongoDB storage failure, or other unexpected errors


### ⚙️ Implementation Notes
Uploaded files are stored under data/docs/ with a timestamp appended to avoid filename collisions.

The document parser returns a list of pages as (page_number, text) tuples.

Theme extraction is optional; failure to extract themes does not block the upload.

Vector ingestion failures are logged but do not affect the main upload success response.