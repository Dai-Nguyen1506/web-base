from fastapi import FastAPI

from app.core.config import settings
from app.core.exceptions import CustomAppException, global_app_exception_handler

from app.api.v1.api import api_router

app = FastAPI(title=settings.PROJECT_NAME,
              version="1.0.0")

app.include_router(api_router, prefix=settings.API_V1_STR)
app.add_exception_handler(CustomAppException, global_app_exception_handler)

@app.get("/")
def read_root():
    return {"message": "hello world"}
