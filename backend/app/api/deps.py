from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.user import User
from app.schemas.token import TokenData
from app.core.security import secret_key, algorithm

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

def get_current_user(
        db: Session = Depends(get_db),
        token: str = Depends(oauth_scheme)
    ) -> User:
    """
    Hàm xác thực danh tính của user qua token
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Không thể xác thực thông tin đăng nhập",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        user_id: str = payload.get("sub")

        if user_id is None:
            raise credentials_exception

        token_data = TokenData(user_id=user_id)
    except:
        raise credentials_exception

    user = db.query(User).filter(User.id == int(token_data.user_id)).first()
    if user is None:
        raise credentials_exception

    return user