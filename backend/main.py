# main.py
# File khởi chạy chính của ứng dụng FastAPI.
# 
# Các bước bạn cần làm:
# 1. Import FastAPI: from fastapi import FastAPI
# 2. Khởi tạo app: app = FastAPI(title="Web Base API")
# 3. Cấu hình CORS middleware cho phép frontend truy cập.
# 4. Include các router từ thư mục api: app.include_router(api_router, prefix=settings.API_V1_STR)
#
# Lệnh chạy: uvicorn main:app --reload
