from users.domain.token import EncryptedToken
from users.application.auth_facade import AuthFacade


class LoginUserUseCase:

    facade : AuthFacade

    def __init__(
            self,
            facade : AuthFacade
        ) -> None:
        self.facade = facade

    async def execute( self, email : str, password: str ) -> EncryptedToken:
        token: EncryptedToken = await self.facade.login(
            email,
            password
        )
        return token
    
    