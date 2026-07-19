from fastapi import FastAPI
from backend.app.api.routes import router

app = FastAPI(
    title="Athena AI",
    version="1.0.0",
)

app.include_router(router)