#!/bin/sh
set -e

echo "=== [1/2] Tự động kiểm tra và nâng cấp Alembic... ==="
alembic upgrade head

echo "=== [2/2] Khởi động Uvicorn với lệnh được chỉ định... ==="
# Chạy chính xác lệnh (uvicorn) được truyền từ Docker Compose
exec "$@"