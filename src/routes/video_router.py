from typing import Annotated

from fastapi import (
    APIRouter,
    Depends
)
from fastapi.responses import JSONResponse

from services.video_service import VideoService
from models.videos import Video
from models.pydantic_models import VideoModel
from dependencies import get_video_service


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
def create_video(video_model: VideoModel, video_service: Annotated[VideoService, Depends(get_video_service)]):
    video = Video(**video_model.dict())
    video_service.create_video(video)
    return video_model


@router.delete("/video/remove/{video_id}")
def delete_video(video_id: str, video_service: Annotated[VideoService, Depends(get_video_service)]):
    return video_service.delete_video(video_id)


@router.put("/video/update/{video_id}", response_model=VideoModel)
def update_video(video_model: VideoModel, video_id: str, video_service: Annotated[VideoService, Depends(get_video_service)]):
    video = Video(**video_model.dict())
    video_service.update_video(video_id, video)
    return video_model