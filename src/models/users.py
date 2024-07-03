from main import connect_to_database


class User:
    """Model to interact with user_collection"""
    def __init__(
        self,
        username: str,
        email: str,
        password: str
    ) -> None:
        self.db = connect_to_database()
        self.user_collection = self.db["users"]
        self.username = username
        self.email = email
        self.password = password
    
    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
    
    def save(self) -> str:
        user_data = self.to_dict()
        result = self.user_collection.insert_one(user_data)
        return result.inserted_id
    
    
    def find_by_username(self, username) -> dict:
        return self.user_collection.find_one({"username": username})
    
    
    def find_by_id(self, user_id) -> dict:
        return self.user_collection.find_one({"_id": user_id})
        
        