from bson.objectid import ObjectId

from src.main import connect_to_database

from models.videos import (
    Video,
    Comment
)


class VideoRepository:
    def __init__(self, video: Video):
        """
        Initialize the user repository.
        """
        self.db = connect_to_database()
        self.video_collection = self.db["videos"]
        self.video = video
    
    
    def add_video(self):
        """Create a new video and add them to the database."""
        video_data = self.video.to_dict()
        result = self.video_collection.insert_one(video_data)
        return result.inserted_id
    
    
    def find_by_id(self, video_id: str):
        """
        Find a video by their ID.
        """
        return self.video_collection.find_one({"_id": ObjectId(video_id)})
    
    
    def find_by_title(self, title: str):
        """Find a video by their title"""
        return self.video_collection.find_one({"title": title})
    
    
    def update_video(self, video_id: str, new_video: Video):
        """Update a video's information"""
        result = self.video_collection.update_one(
            {"_id": ObjectId(video_id)},
            {"$set": new_video.to_dict()}
        )
        return result.modified_count > 0
    
    
    def delete_video(self, video_id):
        """Remove video from database"""
        result = self.video_collection.delete_one({"_id": ObjectId(video_id)})
        
    
    def add_comment(self, video_id: str, comment: Comment):
        """Add comment to video"""
        comment_data = comment.to_dict()
        result = self.video_collection.update_one(
            {"_id": ObjectId(video_id)},
            {"$push": {"comments": comment_data}}
        )
        return result.modified_count > 0


    def list_videos(self) -> list:
        """Get list of videos"""
        return list(self.video_collection.find({}))