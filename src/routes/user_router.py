from typing import Annotated

from fastapi import (
    APIRouter,
    Depends
)

from services.user_service import UserService
from models.users import User
from models.pydantic_models import UserModel
from dependencies import get_user_service
from utils import generate_hash_based_on_string


# User router
router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)


@router.get("/user/{user_id}")
def get_user_by_id(user_id: str, user_service: Annotated[UserService, Depends(get_user_service)]):
    return user_service.get_user_by_id(user_id)


@router.get("/all-users")
def get_all_users(user_service: Annotated[UserService, Depends(get_user_service)]):
    return user_service.get_all_users()


@router.post("/user/add", response_model=UserModel)
def create_user(user_model: UserModel, user_service: Annotated[UserService, Depends(get_user_service)]):
    result_user_model = user_model.dict()
    result_user_model["id"] = generate_hash_based_on_string()
    user = User(**result_user_model)
    user_service.create_user(user)
    return result_user_model


@router.delete("/user/remove/{user_id}")
def delete_user(user_id: str, user_service: Annotated[UserService, Depends(get_user_service)]):
    return user_service.delete_user(user_id)


@router.put("/user/update/{user_id}", response_model=UserModel)
def update_user(user_model: UserModel, user_id: str, user_service: Annotated[UserService, Depends(get_user_service)]):
    result_user_model = user_model.dict()
    result_user_model["id"] = user_id
    user = User(**result_user_model)
    user_service.update_user(user_id, user)
    return result_user_model
    

    
