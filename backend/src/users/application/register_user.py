from users.application.auth_facade import AuthFacade
from users.domain.user import UserRole

class RegisterUserUseCase:

    facade : AuthFacade

    def __init__(
            self,
            facade : AuthFacade
        ) -> None:
        self.facade = facade

    async def execute( self, name: str, email : str, password: str, role : UserRole ):
        await self.facade.register(
            name,
            email,
            password,
            role
        )
        return