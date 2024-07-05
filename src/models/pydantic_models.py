from pydantic import BaseModel


class UserModel(BaseModel):
    username: str
    email: str
    password: str


class VideoModel(BaseModel):
    title: str
    user_id: str
    video_path: str
    description: str
    comments: list
    
    
