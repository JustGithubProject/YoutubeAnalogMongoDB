from bson import ObjectId
from pydantic import (
    BaseModel,
    Field
)



class UserModel(BaseModel):
    username: str
    email: str
    password: str
    

class VideoModel(BaseModel):
    title: str
    user_id: str
    video_path: str
    description: str


class UserLogin(BaseModel):
    username: str
    password: str


