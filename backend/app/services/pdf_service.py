from pathlib import Path
from fastapi import UploadFile

UPLOAD_DIR = Path("backend/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def save_pdf(file: UploadFile):
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return {
        "filename": file.filename,
        "status": "uploaded successfully"
    }