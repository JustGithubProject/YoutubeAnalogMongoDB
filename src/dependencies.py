from fastapi import (
    Depends,
    Query
)
from models.users import User
from models.videos import Video
from models.pydantic_models import (
    UserModel,
    VideoModel
)

from services.user_service import UserService
from services.video_service import VideoService
from repositories.user_repository import UserRepository
from repositories.video_repository import VideoRepository


def get_user_service():
    return UserService(UserRepository())


def get_video_service():
    return VideoService(VideoRepository())
