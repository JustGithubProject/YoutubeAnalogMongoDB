from repositories.video_repository import VideoRepository
from models.videos import (
    Video,
    Comment
)


class VideoService:
    def __init__(self, video_repository: VideoRepository):
        """
        Initialize the video service with a video repository.
        """
        self.video_repository = video_repository
    
    
    def create_video(self, video: Video):
        """
        Create a new video.
        """
        return self.video_repository.add_video(video)
    
    
    def get_video_by_id(self, video_id: str):
        """
        Retrieve a video by its ID.
        """
        return self.video_repository.find_by_id(video_id)
    
    
    def get_video_by_title(self, title: str):
        """
        Retrieve a video by its title.
        """
        return self.video_repository.find_by_title(title)
    
    
    def update_video(self, video_id: str, new_video_data: Video):
        """
        Update a video's information.
        """
        return self.video_repository.update_video(video_id, new_video_data)
    
    
    def delete_video(self, video_id: str):
        """
        Delete a video by its ID.
        """
        return self.video_repository.delete_video(video_id)
    
    
    def add_comment_to_video(self, video_id: str, comment: Comment):
        """
        Add a comment to a video.
        """
        return self.video_repository.add_comment(video_id, comment)
    
    
    def get_all_videos(self):
        """Get all videos"""
        return self.video_repository.list_videos()
