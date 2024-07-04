from repositories.user_repository import UserRepository
from models.users import User


class UserService:
    def __init__(self, user_repository: UserRepository):
        """
        Initialize the user service with a user repository.
        """
        self.user_repository = user_repository
    
    def create_user(self, user: User):
        """
        Create a new user.
        """
        return self.user_repository.add_user(user)
    
    def get_user_by_id(self, user_id: str):
        """
        Retrieve a user by their ID.
        """
        return self.user_repository.find_by_id(user_id)
    
    def get_user_by_username(self, username: str):
        """
        Retrieve a user by their username.
        """
        return self.user_repository.find_by_username(username)
    
    def update_user(self, user_id: str, new_user_data: User):
        """
        Update a user's information.
        """
        return self.user_repository.update_user(user_id, new_user_data)
    
    def delete_user(self, user_id: str):
        """
        Delete a user by their ID.
        """
        return self.user_repository.delete_user(user_id)
    
        
           