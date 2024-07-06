from bson import ObjectId
from pydantic import (
    BaseModel,
    Field
)



class UserModel(BaseModel):
    username: str
    email: str
    password: str
    
    
class UserLogin(BaseModel):
    username: str
    password: str


class UserRegister(BaseModel):
    username: str
    password: str
    email: str
        

class VideoModel(BaseModel):
    title: str
    user_id: str
    video_path: str
    description: str





