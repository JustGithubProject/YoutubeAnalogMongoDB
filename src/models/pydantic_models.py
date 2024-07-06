from bson import ObjectId
from pydantic import (
    BaseModel,
    Field
)



class UserModel(BaseModel):
    id: str
    username: str
    email: str
    password: str
    

class VideoModel(BaseModel):
    id: str
    title: str
    user_id: str
    video_path: str
    description: str
    comments: list
    
    
