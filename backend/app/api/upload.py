from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import shutil
import uuid
from datetime import datetime

from app.services.document_parser import parse_document
from app.database.mongodb import parsed_docs  # 👈 Import the collection

router = APIRouter()

ALLOWED_EXTENSIONS = {".pdf", ".docx", ".png", ".jpg", ".jpeg"}
UPLOAD_DIR = Path("data")
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

    try:
        parsed_text = parse_document(str(file_path))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error parsing document: {str(e)}")

    # Store document in MongoDB
    try:
        parsed_docs.insert_one({
            "original_filename": file.filename,
            "stored_filename": new_filename,
            "file_path": str(file_path),
            "file_extension": ext,
            "parsed_text": parsed_text,
            "upload_time": datetime.now()
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save document in DB: {str(e)}")

    return {
        "message": "File uploaded, parsed, and stored successfully",
        "filename": new_filename,
        "parsed_text_preview": parsed_text[:1000]
    }
