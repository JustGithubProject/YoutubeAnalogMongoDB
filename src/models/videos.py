from main import connect_to_database


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
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "comments": []
        }
    
    def save(self):
        video_data = self.to_dict()
        result = self.video_collection.insert_one(video_data)
        return result.inserted_id


    def find_by_title(self, title):
        return self.video_collection.find_one({"title": title})
    