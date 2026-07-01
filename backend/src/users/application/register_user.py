from users.application.auth_facade import AuthFacade

class RegisterUserUseCase:

    facade : AuthFacade

    def __init__(
            self,
            facade : AuthFacade
        ) -> None:
        self.facade = facade

    async def execute( self, name: str, email : str, password: str ):
        await self.facade.register(
            name,
            email,
            password
        )
        return