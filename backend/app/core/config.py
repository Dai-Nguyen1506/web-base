from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # 1. Cấu hình API chung
    PROJECT_NAME: str = "Web Base"
    API_V1_STR: str = "/api/v1"

    # 2. Cấu hình Bảo mật (JWT)
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # Mặc định là 8 ngày

    # 3. Cấu hình kết nối Cơ sở dữ liệu
    DATABASE_URL: str

    # Chỉ định cấu hình để Pydantic đọc file .env
    model_config = SettingsConfigDict(
        case_sensitive=True,  # Phân biệt chữ hoa/chữ thường giống hoàn toàn với .env
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Bỏ qua nếu trong file .env có những biến thừa không dùng tới ở đây
    )

# Khởi tạo một đối tượng settings duy nhất để dùng chung cho toàn bộ hệ thống Backend
settings = Settings()

# Kiểm tra
if __name__ == '__main__':
    print('Project Name:', settings.PROJECT_NAME)