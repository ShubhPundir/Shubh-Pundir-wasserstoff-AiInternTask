from fastapi import APIRouter
from pydantic import BaseModel
from app.services.query_processor import query_documents

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/query/")
async def query_route(request: QueryRequest):
    result = query_documents(request.query)
    return {"answer": result}
