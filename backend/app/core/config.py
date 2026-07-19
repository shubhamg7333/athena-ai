import os
from dotenv import load_dotenv

load_dotenv("backend/.env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in backend/.env")