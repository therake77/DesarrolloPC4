

from abc import ABC, abstractmethod

from users.domain.user import User, UserEmail, UserId


class UserRepository(ABC):

    @abstractmethod
    async def find_by_id( self, id : UserId)->User | None:
        pass

    @abstractmethod
    async def find_by_email( self, email : UserEmail)-> User | None:
        pass

    @abstractmethod
    async def update_user( self, user : User)->None:
        pass

    @abstractmethod
    async def save_user( self, user : User)->None:
        pass

    @abstractmethod
    async def delete_user( self, id : UserId)->None:
        pass