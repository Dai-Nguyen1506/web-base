from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import hash_password
from app.api.deps import get_current_user
from app.core.exceptions import EmailAlreadyExistsException

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def register_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user_in.email))
    existed_user = result.scalars().first()

    if existed_user:
        raise EmailAlreadyExistsException()
    
    hashed_pwd = hash_password(user_in.password)
    new_user = User(
        email=user_in.email,
        password_hashed=hashed_pwd,
        is_activate=True
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user

@router.post("/me", response_model=UserResponse)
async def read_user_me(current_user: User = Depends(get_current_user)):
    """
    API lấy thông tin người dùng
    """
    return current_user