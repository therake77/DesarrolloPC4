

from abc import ABC, abstractmethod

from users.domain.user import User, UserEmail, UserId
from users.domain.user_notification import UserNotification


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
    async def get_notifications(self, id : UserId) -> list[UserNotification]:
        pass

    @abstractmethod
    async def save_notification(self, notification : UserNotification) -> None:
        pass
    
    @abstractmethod
    async def save_user( self, user : User)->None:
        pass

    @abstractmethod
    async def delete_user( self, id : UserId)->None:
        pass