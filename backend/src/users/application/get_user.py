


from shared.application.uow import UnitOfWork
from users.domain.user import UserId
from users.domain.user_repository import UserRepository


class GetUserInfoUseCase:

    user_repo : UserRepository
    uow : UnitOfWork

    def __init__(
            self,
            user_repo : UserRepository,
            uow : UnitOfWork
        ) -> None:
        self.user_repo = user_repo
        self.uow = uow

    async def execute( self, id : int):
        async with self.uow:
            user = await self.user_repo.find_by_id(UserId(id))
            if (user is None): raise UserNoExistsException
            return user

class UserNoExistsException(Exception) : pass