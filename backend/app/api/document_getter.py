import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import APIRouter
from database.mongodb import parsed_docs

router = APIRouter()

collection = parsed_docs

@router.get("/documents")
async def read_all_files():
    results = []
    print(os.getcwd())

    for doc in collection.find():
        file_path = doc.get("file_path")
        original_filename = doc.get("original_filename") or "Unnamed file"
        doc_id = str(doc.get("_id"))

        file_path = os.path.normpath(file_path)

        if not os.path.exists(os.getcwd() + file_path):
            results.append({
                "id": doc_id,
                "original_filename": original_filename,
                "file_path": os.getcwd() +'\\'+ file_path
            })
            continue
        else:
            results.append({
                "id": doc_id,
                "original_filename": original_filename,
                "error": f'File not found at {file_path}'
            })

    return results
