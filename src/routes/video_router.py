from typing import Annotated

from fastapi import (
    APIRouter,
    Depends
)
from services.video_service import VideoService
from models.videos import Video
from dependencies import get_video_service


# Video router
router = APIRouter()


@router.get("/video/{video_id}")
def get_video_by_id(video_id: str, video_service: Annotated[VideoService, Depends(get_video_service)]):
    return video_service.get_video_by_id(video_id)


@router.get("/all-videos")
def get_all_videos(video_service: Annotated[VideoService, Depends(get_video_service)]):
    return video_service.get_all_videos()


@router.post("/video/add")
def create_video(video: Video, video_service: Annotated[VideoService, Depends(get_video_service)]):
    return video_service.create_video(video)


@router.delete("/video/remove/{video_id}")
def delete_video(video_id: str, video_service: Annotated[VideoService, Depends(get_video_service)]):
    return video_service.delete_video(video_id)


@router.put("/video/update/{video_id}")
def update_video(video_id: str, video_service: Annotated[VideoService, Depends(get_video_service)]):
    return video_service.update_video(video_id)
