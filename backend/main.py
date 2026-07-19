from fastapi import FastAPI
from pydantic import BaseModel
from backend.gemini import generate_response

app = FastAPI(
    title="Athena AI",
    version="1.0.0",
)

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Welcome to Athena AI 🚀"}


@app.post("/chat")
def chat(request: ChatRequest):
    reply = generate_response(request.message)
    return {"response": reply}