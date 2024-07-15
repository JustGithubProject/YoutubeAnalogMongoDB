from config import connect_to_database
from models.users import User

from bson.objectid import ObjectId


class UserRepository:
    def __init__(self):
        """
        Initialize the user repository.
        """
        self.db = connect_to_database()
        self.user_collection = self.db["users"]
    
    
    def add_user(self, user: User):
        """
        Create a new user and add them to the database.
        """
        user_data = user.to_dict()
        result = self.user_collection.insert_one(user_data)
        return result.inserted_id
    
    
    def find_by_id(self, user_id: str):
        """
        Find a user by their ID.
        """
        return self.user_collection.find_one({"_id": str(user_id)})
    
    
    def find_by_username(self, username: str):
        """
        Find a user by their username.
        """
        return self.user_collection.find_one({"username": username})
    
    
    def update_user(self, user_id: str, new_user: User):
        """
        Update a user's information.
        """
        result = self.user_collection.update_one(
            {"_id": str(user_id)},
            {"$set": new_user.to_dict()}
        )
        return result.modified_count > 0
    
    
    def update_user_liked_video(self, user_id: str, user_dict: dict):
        """Update liked video of current_user"""
        self.user_collection.update_one(
            {"_id": str(user_id)},
            {"$set": user_dict}
        )
    
    
    def delete_user(self, user_id: str):
        """Remove user from database"""
        result = self.user_collection.delete_one({"_id": str(user_id)})
        return result.deleted_count > 0
    
    
    def list_user(self) -> list:
        """Get list of users"""
        return list(self.user_collection.find({}))
    