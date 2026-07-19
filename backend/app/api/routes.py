from fastapi import APIRouter, UploadFile, File

from backend.app.schemas.chat import ChatRequest
from backend.app.services.gemini import generate_response
from backend.app.services.pdf_service import save_pdf

router = APIRouter()


@router.get("/")
def home():
    return {"message": "Welcome to Athena AI 🚀"}


@router.post("/chat")
def chat(request: ChatRequest):
    reply = generate_response(request.message)
    return {"response": reply}


@router.post("/upload")
def upload_pdf(file: UploadFile = File(...)):
    return save_pdf(file)