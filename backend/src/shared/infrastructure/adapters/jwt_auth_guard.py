

from shared.application.uow import UnitOfWork
from shared.domain.auth_guard import AuthGuard
from users.domain.token import EncryptedToken, Token
from users.domain.token_handler import TokenHandler
from users.domain.user_repository import UserRepository


class JWTAuthGuard(AuthGuard):
    token_handler : TokenHandler
    user_repo : UserRepository

    def __init__(
            self,
            token_handler : TokenHandler,
            user_repo : UserRepository,
            uow : UnitOfWork
        ) -> None:
        self.token_handler = token_handler 
        self.user_repo = user_repo
        self.uow = uow

    async def resolve_token(self,encrypted_token : EncryptedToken):
        print("Inside guard")
        token : Token =  self.token_handler.decode_token(encrypted_token)
        print("After decryption")
        async with self.uow:
            user = await self.user_repo.find_by_id(token.user_id)
        print(user)
        if user is None:
            raise Exception("Unauthorized")
        print(user)
        return user