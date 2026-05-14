# app/core/config.py
# Sử dụng Pydantic BaseSettings để quản lý biến môi trường.
# 
# Ví dụ:
# from pydantic_settings import BaseSettings
#
# class Settings(BaseSettings):
#     PROJECT_NAME: str = "Web Base"
#     API_V1_STR: str = "/api/v1"
#     POSTGRES_SERVER: str
#     POSTGRES_USER: str
#     POSTGRES_PASSWORD: str
#     POSTGRES_DB: str
# 
#     class Config:
#         env_file = ".env"
#
# settings = Settings()
