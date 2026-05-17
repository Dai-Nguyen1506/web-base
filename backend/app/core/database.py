from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

# 1. Lấy chuỗi kết nối từ biến môi trường (Docker đã tự động truyền vào)
DATABASE_URL = settings.DATABASE_URL

# 2. Cấu hình Connection Pool tối ưu cho hiệu năng và độ ổn định
engine = create_engine(
    DATABASE_URL,
    pool_size=10,          # Giữ tối đa 10 kết nối luôn mở sẵn trong bộ nhớ để dùng ngay
    max_overflow=10,       # Khi tải tăng đột biến, cho phép mở thêm tối đa 10 kết nối tạm thời
    pool_timeout=30,       # Nếu pool bị đầy, request phải chờ tối đa 30 giây trước khi báo lỗi timeout
    pool_pre_ping=True,    # Cơ chế "bắt tay trước" - tự động kiểm tra kết nối còn sống không trước khi giao cho app
)

# 3. Tạo một nhà máy sản xuất Session (Phiên làm việc với Database)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Tạo lớp nền tảng (Base) để các Model thực thể (User, Product,...) kế thừa sau này
Base = declarative_base()

# 5. Hàm Dependency (Bắt buộc phải có cho FastAPI) để quản lý vòng đời của kết nối
def get_db():
    """
    Hàm này tạo ra một phiên kết nối mới cho mỗi Request và tự động 
    đóng kết nối đó lại sau khi Request xử lý xong (dù thành công hay gặp lỗi).
     giúp ngăn chặn triệt để tình trạng rò rỉ kết nối (Connection Leak).
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()