from bson import ObjectId
from pydantic import (
    BaseModel,
    Field
)



class UserModel(BaseModel):
    username: str
    email: str
    password: str


class UserOut(UserModel):
    id: str
    
    
class UserLogin(BaseModel):
    username: str
    password: str


class UserRegister(UserModel):
    pass

        
class VideoModel(BaseModel):
    title: str
    user_id: str
    video_path: str
    description: str





