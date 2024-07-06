class User:
    """Model to interact with user_collection"""
    def __init__(
        self,
        id: str,
        username: str,
        email: str,
        password: str
    ) -> None:
        self._id = id
        self.username = username
        self.email = email
        self.password = password
    
    def to_dict(self) -> dict:
        return {
            "_id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
    
        
        