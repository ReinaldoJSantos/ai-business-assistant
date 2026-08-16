from fastapi import FastAPI

from app.core.config import settings
from app.api.v1.users import router as users_router

app = FastAPI(
    title="API Business Assistent",
    version="0.1.0"
)
app.include_router(
    users_router,
    prefix="/api/v1",
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