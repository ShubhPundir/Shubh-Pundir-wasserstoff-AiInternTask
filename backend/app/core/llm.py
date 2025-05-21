import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import get_GEMINI_API_KEY

from langchain_google_genai import ChatGoogleGenerativeAI
# load_dotenv()

def get_gemini_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=get_GEMINI_API_KEY(),
        temperature=0.3
    )
