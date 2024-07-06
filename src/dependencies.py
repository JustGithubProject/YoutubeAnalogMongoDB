from datetime import datetime

from fastapi import (
    Depends,
    HTTPException,
    status
)

from pydantic import ValidationError

from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from models.pydantic_models import UserOut
from services.user_service import UserService
from services.video_service import VideoService
from repositories.user_repository import UserRepository
from repositories.video_repository import VideoRepository

from auth.schemas import TokenPayload

from config import (
    JWT_REFRESH_SECRET_KEY,
    JWT_SECRET_KEY,
    ALGORITHM
)


reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
)


def get_current_user(token: str = Depends(reuseable_oauth)):
    try:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)
        
        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    user_service = get_user_service()
    user = user_service.find_by_username(token_data.name, None)
    
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    
    return UserOut(**user)


def get_user_service():
    return UserService(UserRepository())


def get_video_service():
    return VideoService(VideoRepository())
