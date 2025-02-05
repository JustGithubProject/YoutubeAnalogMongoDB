import os

from typing import Annotated
from uuid import uuid4

from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    Form,
    Query
)
from fastapi.responses import JSONResponse

from services.video_service import VideoService
from services.user_service import UserService
from models.videos import (
    Video,
    Comment
)
from models.pydantic_models import VideoModel
from dependencies import get_video_service

from dependencies import (
    get_current_user,
    get_user_service
)
from models.users import User
from utils import save_file


# Video router
router = APIRouter(
    prefix="/video",
    tags=["videos"],
    responses={404: {"description": "Not found"}}
)


@router.get("/video/{video_id}")
def get_video_by_id(video_id: str, video_service: Annotated[VideoService, Depends(get_video_service)]):
    return video_service.get_video_by_id(video_id)


@router.get("/video/search/")
def get_video_by_title(
    video_service: Annotated[VideoService, Depends(get_video_service)],
    video_title_query: str = Query(..., min_length=2)):
    return video_service.get_video_by_title(video_title_query)


@router.get("/all-videos")
def get_all_videos(video_service: Annotated[VideoService, Depends(get_video_service)]):
    return video_service.get_all_videos()


@router.post("/video/add", response_model=VideoModel)
def create_video(
    title: Annotated[str, Form()],
    description: Annotated[str, Form()],
    preview_image_path: Annotated[UploadFile, File()],
    video_path: Annotated[UploadFile, File(...)],
    video_service: Annotated[VideoService, Depends(get_video_service)],
    current_user: User = Depends(get_current_user),
    ):
    video_id = str(uuid4())
    user_id = str(current_user["_id"])
    preview_id = str(uuid4())
    
    # Getting bytes
    preview_image_bytes = preview_image_path.file.read()
    video_bytes = video_path.file.read()
    
    # Save preview image
    preview_full_path = save_file(preview_image_path, preview_image_bytes)
      
    # Save video file
    video_full_path = save_file(video_path, video_bytes)
    
    video_data = {
        "id": video_id,
        "title": title,
        "user_id": user_id,
        "description": description,
        "video_path": video_full_path,
        "preview_image_path": preview_full_path
    }
    
    video = Video(**video_data)
    
    video_service.create_video(video)
    return video_data



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



@router.post("/video/add/comment/{video_id}")
def create_comment(
    video_id: str,
    comment: str,
    video_service: Annotated[VideoService, Depends(get_video_service)],
    current_user: User = Depends(get_current_user),
):
    comment_model = Comment(current_user["_id"], video_id, current_user["username"], comment)
    video_service.add_comment_to_video(video_id, comment_model)
    return comment_model.to_dict()


@router.post("/video/like/{video_id}")
def increase_like(
    video_id: str,
    video_service: Annotated[VideoService, Depends(get_video_service)],
    user_service: Annotated[UserService, Depends(get_user_service)],
    current_user: User = Depends(get_current_user)
):
    # Did the current user like this video?
    if video_id in current_user["liked"]:
        return "You already liked"
    
    # Adding video_id to list of current_user
    current_user["liked"].append(video_id)
    user_service.update_user_liked_video(current_user["_id"], current_user)
    video_service.add_like(video_id)
    return "Successfully added"


@router.post("/video/put-away-like/{video_id}")
def decrease_like(
    video_id: str,
    video_service: Annotated[VideoService, Depends(get_video_service)],
    user_service: Annotated[UserService, Depends(get_user_service)],
    current_user: User = Depends(get_current_user)
):
    if video_id in current_user["liked"]:
        current_user["liked"].remove(video_id)
        user_service.update_user_liked_video(current_user["_id"], current_user)
        video_service.minus_like(video_id)
        return "Success"
    else:
        return "Fail"
    
    
@router.post("/video/view/{video_id}")
def increase_view(
    video_id: str,
    video_service: Annotated[VideoService, Depends(get_video_service)],
):
    video_service.add_view(video_id)
    return "Successfully added"


