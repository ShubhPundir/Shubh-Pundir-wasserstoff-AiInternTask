import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

def get_GEMINI_API_KEY():
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    return GEMINI_API_KEY

def get_MONGO_ATLAS_URI():
    MONGO_ATLAS_URI: str = os.getenv("MONGO_ATLAS_URI")
    return MONGO_ATLAS_URI

def get_VECTOR_DB_PATH():
    VECTOR_DB_PATH: str = os.getenv("VECTOR_DB_PATH")
    return VECTOR_DB_PATH
