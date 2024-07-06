from typing import Annotated
from uuid import uuid4

from fastapi import (
    APIRouter,
    Depends
)
from fastapi.responses import JSONResponse

from services.video_service import VideoService
from models.videos import Video
from models.pydantic_models import VideoModel
from dependencies import get_video_service

from dependencies import get_current_user
from models.users import User


# Video router
router = APIRouter(
    prefix="/video",
    tags=["videos"],
    responses={404: {"description": "Not found"}}
)


@router.get("/video/{video_id}")
def get_video_by_id(video_id: str, video_service: Annotated[VideoService, Depends(get_video_service)]):
    return video_service.get_video_by_id(video_id)


@router.get("/all-videos")
def get_all_videos(video_service: Annotated[VideoService, Depends(get_video_service)]):
    return video_service.get_all_videos()


@router.post("/video/add", response_model=VideoModel)
def create_video(
    video_model: VideoModel,
    video_service: Annotated[VideoService, Depends(get_video_service)],
    current_user: User = Depends(get_current_user),
    ):
    result_video_model = video_model.dict()
    result_video_model["id"] = str(uuid4())
    video = Video(**result_video_model)
    video_service.create_video(video)
    return result_video_model


@router.delete("/video/remove/{video_id}")
def delete_video(
    video_id: str,
    video_service: Annotated[VideoService, Depends(get_video_service)],
    current_user: User = Depends(get_current_user),
):
    return video_service.delete_video(video_id)


@router.put("/video/update/{video_id}", response_model=VideoModel)
def update_video(
    video_model: VideoModel,
    video_id: str,
    video_service: Annotated[VideoService, Depends(get_video_service)],
    current_user: User = Depends(get_current_user),
):
    result_video_model = video_model.dict()
    result_video_model["id"] = video_id
    video = Video(**result_video_model)
    video_service.update_video(video_id, video)
    return result_video_model