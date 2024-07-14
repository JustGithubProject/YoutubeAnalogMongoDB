import hashlib
import random
import string

from datetime import datetime

from config import connect_to_database

def generate_string():
    letters = string.ascii_letters
    return "".join([random.choice(letters) for _ in range(10)])    


class Comment:
    """Model to interact with comment"""
    def __init__(
        self,
        user_id: str,
        video_id: str,
        username: str,
        comment: str
    ) -> None:
        self.user_id = user_id
        self.username = username
        self.video_id = video_id
        self.comment = comment
        self.timestamp = datetime.utcnow()
    
    
    def to_dict(self):
        return {
            "video_id": self.video_id,
            "user_id": self.user_id,
            "username": self.username,
            "comment": self.comment,
            "timestamp": self.timestamp,
        }
    


class Video:
    """Model to interact with video collection"""
    def __init__(
        self,
        id: str,
        title: str,
        preview_image_path: str,
        user_id: str,
        video_path: str,
        description: str,
    ) -> None:
        self.db = connect_to_database()
        self.video_collection = self.db["videos"]
        self._id = id 
        self.title = title
        self.preview_image_path = preview_image_path
        self.user_id = user_id
        self.video_path = video_path
        self.description = description
    
    
    def to_dict(self) -> dict:
        return {
            "_id": self._id,
            "title": self.title,
            "user_id": self.user_id,
            "video_path": self.video_path,
            "preview_image_path": self.preview_image_path,
            "description": self.description,
            "views": 0,
            "likes": 0,
            "comments": []
        }
    
    



