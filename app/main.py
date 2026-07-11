from fastapi import FastAPI

app = FastAPI(
    title="API Business Assistent",
    version="0.1.0"
)

@app.get('/')
def root():
    return {"message": "Projeto iniciado com sucesso!"}

@app.get("/health")
def health():
    return {"status": "ok"}