from abc import ABC, abstractmethod

from users.domain.token import EncryptedToken, Token
from users.domain.user import User


class TokenHandler(ABC):

    @abstractmethod
    def create_token(self, user : User) -> EncryptedToken:
        pass
    
    @abstractmethod
    def decode_token(self, token : EncryptedToken) -> Token:
        pass