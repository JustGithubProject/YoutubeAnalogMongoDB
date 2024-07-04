from main import connect_to_database
from models.users import User

from bson.objectid import ObjectId


class UserRepository:
    def __init__(self, user: User):
        """
        Initialize the user repository.
        """
        self.db = connect_to_database()
        self.user_collection = self.db["users"]
        self.user = user
    
    def add_user(self):
        """
        Create a new user and add them to the database.
        """
        user_data = self.user.to_dict()
        result = self.user_collection.insert_one(user_data)
        return result.inserted_id
    
    def find_by_id(self, user_id: str):
        """
        Find a user by their ID.
        """
        return self.user_collection.find_one({"_id": ObjectId(user_id)})
    
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
            {"_id": ObjectId(user_id)},
            {"$set": new_user.to_dict()}
        )
        return result.modified_count > 0
    
    def delete_user(self, user_id: str):
        """Remove user from database"""
        result = self.user_collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0