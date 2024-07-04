


class User:
    """Model to interact with user_collection"""
    def __init__(
        self,
        username: str,
        email: str,
        password: str
    ) -> None:
        self.username = username
        self.email = email
        self.password = password
    
    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
    
        
        