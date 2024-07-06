from typing import Annotated

from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    status
)

from models.pydantic_models import UserLogin

from services.user_service import UserService
from dependencies import get_user_service
from auth.password_hashing import verify_password
from auth.generate_jwt_token import (
    create_access_token,
    create_refresh_token
)


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}}
)


@auth_router.post("/login")
def login(user_model: UserLogin, user_service: Annotated[UserService, Depends(get_user_service)]):
    user = user_service.get_user_by_username(user_model.username)
    if not UserWarning:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password"
        )
    hashed_password = user["password"]
    if not verify_password(user_model.password, hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password"
        )
    return {
        "access_token": create_access_token(user['username']),
        "refresh_token": create_refresh_token(user['username']),
    }
    