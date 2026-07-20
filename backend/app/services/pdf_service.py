from pathlib import Path
from fastapi import UploadFile

from backend.app.parsers.pdf_parser import extract_text
from backend.app.rag.text_chunker import chunk_text
from backend.app.database.vector_store import add_chunks
UPLOAD_DIR = Path("backend/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def save_pdf(file: UploadFile):
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    extracted_text = extract_text(str(file_path))
    chunks = chunk_text(extracted_text)
    add_chunks(chunks)
    return {
        "filename": file.filename,
        "status": "uploaded successfully",
        "characters": len(extracted_text),
        "chunks": len(chunks),
        "preview": chunks[0] if chunks else ""
    }