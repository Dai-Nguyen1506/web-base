from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title="Web Developer Base")

@app.get("/")
def read_root():
    return {"message": "hello world"}
