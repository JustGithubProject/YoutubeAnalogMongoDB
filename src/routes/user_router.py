from typing import Annotated

from fastapi import (
    APIRouter,
    Depends
)
from services.user_service import UserService
from models.users import User
from dependencies import get_user_service


# User router
router = APIRouter()


@router.get("/user/{user_id}")
def get_user_by_id(user_id: int, user_service: Annotated[UserService, Depends(get_user_service)]):
    return user_service.get_user_by_id(user_id)


@router.get("/all-users")
def get_all_users(user_service: Annotated[UserService, Depends(get_user_service)]):
    return user_service.get_all_users()


@router.post("/user/add")
def create_user(user: User, user_service: Annotated[UserService, Depends(get_user_service)]):
    return user_service.create_user(user)


@router.delete("/user/remove/{user_id}")
def delete_user(user_id: str, user_service: Annotated[UserService, Depends(get_user_service)]):
    return user_service.delete_user(user_id)



@router.put("/user/update/{user_id}")
def update_user(user: User, user_id: str, user_service: Annotated[UserService, Depends(get_user_service)]):
    return user_service.update_user(user_id, user)

    

    
