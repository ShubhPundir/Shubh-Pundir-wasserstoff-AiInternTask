import sys
import os
import mimetypes
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.responses import FileResponse
from fastapi import APIRouter, HTTPException


from core.mongodb import parsed_docs

router = APIRouter()

collection = parsed_docs

@router.get("/documents")
async def read_all_files():
    results = []
    # print(os.getcwd())

    for doc in collection.find():
        file_path = doc.get("file_path")
        original_filename = doc.get("original_filename") or "Unnamed file"
        doc_id = str(doc.get("_id"))
        timestamp = doc.get("upload_time")
        file_path = os.path.normpath(file_path)

        if not os.path.exists(os.getcwd() + file_path):
            results.append({
                "id": doc_id,
                "original_filename": original_filename,
                "timestamp": timestamp,
                # "file_path": os.getcwd() +'\\'+ file_path
                "file_path": file_path
            })
            continue
        else:
            results.append({
                "id": doc_id,
                "original_filename": original_filename,
                "timestamp": timestamp,
                "error": f'File not found at {file_path}'
            })

    return results


@router.get("/open")
async def open_file(path: str):
    file_path = os.path.normpath(path)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    # Guess MIME type (e.g., application/pdf)
    mime_type, _ = mimetypes.guess_type(file_path)

    return FileResponse(
        path=file_path,
        media_type=mime_type or "application/octet-stream"
        # Don't set 'filename' if you want to view, not download
    )
