from google import genai
from backend.app.core.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_response(prompt: str) -> str:
    response = client.models.generate_content(
        model="models/gemini-3.5-flash",
        contents=prompt,
    )

    return response.text if response.text else "No text returned."
