from fastapi import (
    Depends,
    Query
)
from models.users import User
from services.user_service import UserService
from repositories.user_repository import UserRepository


def get_user(
    username: str = Query(...),
    email: str = Query(...),
    password: str = Query(...)
) -> User:
    return User(username, email, password)
    


def get_user_service(user: User = Depends(get_user)):
    return UserService(UserRepository(user))
