from typing import Annotated
from uuid import uuid4

from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    status
)

from models.pydantic_models import (
    UserLogin,
    UserRegister
)

from models.users import User

from services.user_service import UserService
from dependencies import get_user_service
from auth.password_hashing import (
    verify_password,
    get_hashed_password
)

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
    
    # If user doesn't exist, throw an exception
    if not user:
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


@auth_router.post("/register")
def register(user_model: UserRegister, user_service: Annotated[UserService, Depends(get_user_service)]):
    user = user_service.get_user_by_username(user_model.username)
    
    # if the user already exists, throw an exception
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )
    # Hashing the password
    hashed_password = get_hashed_password(user.password)
    
    # Getting dict of pydantic model
    dict_user_model = user_model.dict()
    
    # Adding new values ​​to this dict
    dict_user_model["password"] = hashed_password
    dict_user_model["id"] = str(uuid4())
    
    # Creating new user
    user = User(**dict_user_model)
    user_service.create_user(user)
    
    return dict_user_model