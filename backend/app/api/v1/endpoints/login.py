from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import get_db
from app.models.user import User
from app.core.security import create_access_token, verify_password
from app.schemas.token import Token
from app.core.exceptions import InvalidLoginException

router = APIRouter()

@router.post("/", response_model=Token)
async def login_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: AsyncSession = Depends(get_db)
):
    """
    Đăng nhập hệ thống, sử dụng jwt để xác nhận người dùng
    Đồng thời kiểm soát thời lượng truy cập web
    """
    result = await db.execute(select(User).where(User.email == form_data.username))
    user = result.scalars().first()

    if not user or not user.is_activate or not verify_password(form_data.password, user.password_hashed):
        raise InvalidLoginException()
    
    access_token = create_access_token(subject=user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }