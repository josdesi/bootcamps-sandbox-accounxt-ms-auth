from abc import ABC, abstractmethod
from app.model.login_model import LoginCredentials

class ILoginBusiness(ABC):
    @abstractmethod
    def authenticate(self, credentials: LoginCredentials):
        """Authenticate user credentials"""
        pass