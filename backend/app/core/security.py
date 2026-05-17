from datetime import datetime, timedelta, timezone
from typing import Any, Union
from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

secret_key = settings.SECRET_KEY
algorithm = settings.ALGORITHM
timeaccess = settings.ACCESS_TOKEN_EXPIRE_MINUTES
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hàm băm mật khẩu
    """
    return pwd_context.hash(password)

def verify_password(input_password: str, hashed_password: str) -> bool:
    """
    Hàm kiểm tra mật khẩu
    """
    return pwd_context.verify(input_password, hashed_password)

def create_access_token(subject: Union[str, Any]) -> str:
    """
    Hàm tạo token access cho jwt khi User đăng nhập thành công
    """
    # Tính toán thời gian hết hạn của mã token
    expire = datetime.now(timezone.utc) + timedelta(minutes=timeaccess)

    # Gói thông tin và Payload
    to_encode = {
        "exp": expire,
        "sub": str(subject)
    }

    # Ký bảo mật và sinh chuỗi token JWT
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)

    return encoded_jwt
