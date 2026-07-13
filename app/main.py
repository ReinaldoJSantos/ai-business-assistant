from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(
    title="API Business Assistent",
    version="0.1.0"
)

@app.get('/')
def root():
    return {"message": "Bem-vindo ao AI Business Assistent"}

@app.get("/health")
def health():
    return {
        "status": "ok",
        "application": settings.APP_NAME
        }