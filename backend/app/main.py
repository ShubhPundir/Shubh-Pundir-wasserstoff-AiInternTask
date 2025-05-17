from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import upload

app = FastAPI(title="Gen-AI Document Research Chat Query")

# Enable CORS for frontend (if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Replace with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the Gen-AI Research Chat Query API"}

# Register upload route
app.include_router(upload.router, prefix="/api")