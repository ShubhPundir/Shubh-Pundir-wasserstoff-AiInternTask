import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

class Settings:
    OPENAI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    VECTOR_DB_PATH: str = os.getenv("VECTOR_DB_PATH", "data/vector_db")

settings = Settings()
