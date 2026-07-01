from shared.application.uow import UnitOfWork
from users.domain.user import HashedPassword, User, UserRole

from users.domain.user import UserCredentials, UserEmail, UserId, UserName
from users.domain.user_repository import UserRepository
from users.domain.hash_strategy import HashStrategy
from users.domain.token import EncryptedToken
from users.domain.token_handler import TokenHandler


class AuthFacade:

    token_handler : TokenHandler
    hash_provider : HashStrategy
    user_repo : UserRepository
    uow : UnitOfWork


    def __init__(
        self,
        token_handler : TokenHandler,
        hash_provider : HashStrategy,
        user_repo : UserRepository,
        uow : UnitOfWork
    ) -> None:
        self.token_handler = token_handler
        self.hash_provider = hash_provider
        self.user_repo = user_repo
        self.uow = uow

    async def login( self, email : str, password: str ) -> EncryptedToken:
        user: User | None = await self.user_repo.find_by_email(UserEmail(email))
        if user is None: raise UserNotFoundException

        if(not self.hash_provider.compare_hash(password,user.credentials.hashed_password)):
            raise UnauthorizedException

        return self.token_handler.create_token(user)

    async def register( self, name : str, email : str, password : str, role : UserRole ) -> None:
        
        hashed_password: HashedPassword = self.hash_provider.hash(password)
        try:
            async with self.uow:
                await self.user_repo.save_user(
                    User(
                        uid=UserId(0),
                        name=UserName(name),
                        credentials=UserCredentials(UserEmail(email),hashed_password),
                        role=role
                    )
                )
        except Exception as e:
            print(e.__str__())
            raise UnprocessableRegisterException("Unsuccessfull register")

        return


class UserNotFoundException(Exception) : pass
class UnprocessableRegisterException(Exception): pass
class UnauthorizedException(Exception) : pass