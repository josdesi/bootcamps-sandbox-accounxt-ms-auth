from abc import ABC, abstractmethod
from typing import Optional, Dict

class UsersAuthRepository(ABC):
    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[Dict]:
        """Retrieve user by email from the auth storage"""
        pass

    def get_user_by_username(self, username):
        pass