

from shared.application.uow import UnitOfWork
from users.domain.user import UserId
from users.domain.user_repository import UserRepository


class GetUserNotificationsUseCase:

    uow : UnitOfWork
    user_repo : UserRepository

    def __init__(
            self,
            uow : UnitOfWork,
            user_repo : UserRepository
        ) -> None:
        self.uow = uow
        self.user_repo = user_repo

    async def execute(self, user_id : int):
        async with self.uow:
            notifications = await self.user_repo.get_notifications(UserId(user_id))
        return notifications