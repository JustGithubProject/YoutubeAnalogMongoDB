from typing import Annotated
from uuid import uuid4

from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    Form
)
from fastapi.responses import JSONResponse

from services.video_service import VideoService
from models.videos import (
    Video,
    Comment
)
from models.pydantic_models import VideoModel
from dependencies import get_video_service

from dependencies import get_current_user
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


@router.get("/all-videos")
def get_all_videos(video_service: Annotated[VideoService, Depends(get_video_service)]):
    return video_service.get_all_videos()


@router.post("/video/add", response_model=VideoModel)
def create_video(
    title: Annotated[str, Form()],
    description: Annotated[str, Form()],
    video_path: Annotated[UploadFile, File(...)],
    video_service: Annotated[VideoService, Depends(get_video_service)],
    current_user: User = Depends(get_current_user),
    ):
    video_id = str(uuid4())
    user_id = str(current_user._id)
    
    
    # Saving a file that the user has selected
    file_location = f"videos/{video_id}_{video_path.filename}"
    path_to_file = save_file(file_location, video_path)
    
    
    video_data = {
        "title": title,
        "user_id": user_id,
        "description": description,
        "video_path": path_to_file
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