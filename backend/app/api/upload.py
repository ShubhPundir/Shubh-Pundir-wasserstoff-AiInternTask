from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import shutil
from datetime import datetime

from app.services.document_parser import parse_document
from app.core.mongodb import parsed_docs
from app.services.vector_ingest import ingest_to_qdrant
from app.services.theme_analyzer import extract_themes_from_document

router = APIRouter()

ALLOWED_EXTENSIONS = {".pdf", ".docx", ".png", ".jpg", ".jpeg"}
UPLOAD_DIR = Path("data/docs")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"File type '{ext}' not supported.")

    # Unique filename
    timestamp = datetime.now().strftime("_%Y%m%d_%H%M%S")
    new_filename = f"{Path(file.filename).stem}{timestamp}{ext}"
    file_path = UPLOAD_DIR / new_filename

    # Save file to disk
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        print(f"    File {file.filename} saved to /data/docs as {new_filename}")

    try:
        parsed_pages = parse_document(str(file_path))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing document: {str(e)}")

    flat_text = "\n".join([text for _, text in parsed_pages])
    
    # Extract themes from the flattened text
    try:
        themes = extract_themes_from_document(flat_text)
        print(f"    Extracted themes: {themes}")
    except Exception as e:
        # If theme extraction fails, continue without themes or handle as needed
        print(f"Theme extraction failed: {str(e)}")
        themes = []
    
    # Store document in MongoDB
    try:

        result = parsed_docs.insert_one({
            "original_filename": file.filename,
            "stored_filename": new_filename,
            "file_path": str(file_path),
            "file_extension": ext,
            "parsed_text": flat_text,
            "upload_time": datetime.now(),
            "themes" : themes
        })

        inserted_id = str(result.inserted_id)
        print(f"    MongoDB document stored")


    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save document in DB: {str(e)}")

    try:
        ## Module to ingest into vector store
        ingest_to_qdrant(inserted_id, parsed_pages, "docs")
        print(f"    Vector Embeddings for {inserted_id} has been stored")
    except Exception as e:
        print(f"Vector store ingestion failed: {str(e)}")

    return {
        "message": "File uploaded, parsed, and stored successfully",
        "filename": new_filename,
        "document_id": inserted_id
    }
