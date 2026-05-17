from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User
from app.core.security import create_access_token, verify_password
from app.schemas.token import Token

router = APIRouter()

@router.post("/", response_model=Token)
def login_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
):
    """
    Đăng nhập hệ thống, sử dụng jwt để xác nhận người dùng
    Đồng thời kiểm soát thời lượng truy cập web
    """
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user or not user.is_activate:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email hoặc mật khẩu không đúng")
    
    if not verify_password(form_data.password, user.password_hashed):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Mật khẩu không chính xác")
    
    access_token = create_access_token(subject=user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }