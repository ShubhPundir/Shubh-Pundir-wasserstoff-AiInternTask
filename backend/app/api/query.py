from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.query_processor import query_documents

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/query/")
async def query_route(request: QueryRequest):
    try:
        result = query_documents(request.query)
        return {"answer": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query processing failed: {str(e)}")
