from datetime import datetime

from main import connect_to_database



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
            "user_id": self.user_id,
            "video_id": self.video_id,
            "username": self.username,
            "comment": self.comment,
            "timestamp": self.timestamp
        }
    


class Video:
    """Model to interact with video collection"""
    def __init__(
        self,
        title: str,
        user_id: str,
        description: str,
    ) -> None:
        self.db = connect_to_database()
        self.video_collection = self.db["videos"]
        self.title = title
        self.user_id = user_id
        self.description = description
    
    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "user_id": self.user_id,
            "comments": []
        }
    
    def save(self) -> str:
        video_data = self.to_dict()
        result = self.video_collection.insert_one(video_data)
        return result.inserted_id


    def find_by_title(self, title) -> dict:
        return self.video_collection.find_one({"title": title})
    
    def add_comment(self, comment: Comment):
        update_result = self.videos_collection.update_one(
        {"_id": comment.video_id},
        {
            "$push": {
                "comments": comment.to_dict()
            }
        }
        )
        return update_result
    



