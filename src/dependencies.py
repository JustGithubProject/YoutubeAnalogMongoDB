from fastapi import (
    Depends,
    Query
)
from models.users import User
from models.videos import Video
from services.user_service import UserService
from services.video_service import VideoService
from repositories.user_repository import UserRepository


def get_user(
    username: str = Query(...),
    email: str = Query(...),
    password: str = Query(...)
) -> User:
    return User(
        username=username,
        email=email,
        password=password
    )



def get_user_service(user: User = Depends(get_user)):
    return UserService(UserRepository(user))


def get_video(
    title: str = Query(...),
    user_id: str = Query(...),
    video_path: str = Query(...),
    description: str = Query(...),
    
) -> Video:
    return Video(
        title=title,
        user_id=user_id,
        video_path=video_path,
        description=description
    )


def get_video_service(video: Video = Depends(get_video)):
    return VideoService(video)
