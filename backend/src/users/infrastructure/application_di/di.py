
from fastapi import Depends

from shared.application.uow import UnitOfWork
from users.application.get_user import GetUserInfoUseCase
from users.infrastructure.adapters.di import get_sql_user_repo
from shared.infrastructure.adapters.di import get_sql_unit_of_work
from shared.infrastructure.adapters.sql_uow import SQLUnitOfWork
from users.application.auth_facade import AuthFacade
from users.application.login_user import LoginUserUseCase
from users.application.register_user import RegisterUserUseCase
from users.domain.user_repository import UserRepository
from users.infrastructure.adapters.bcrypt_hash_strategy import BcryptHashStrategy
from users.infrastructure.adapters.jwt_token_handler import JwtTokenHandler



async def get_sql_auth_facade( 
    user_repo: UserRepository = Depends(get_sql_user_repo), 
    uow: SQLUnitOfWork = Depends(get_sql_unit_of_work)
):
    return AuthFacade(
        JwtTokenHandler(),
        BcryptHashStrategy(),
        user_repo,
        uow
    )

async def get_login_user_uc(
    auth_facade : AuthFacade = Depends(get_sql_auth_facade)
):
    return LoginUserUseCase(
        auth_facade
    )

async def get_register_user_uc(
    auth_facade : AuthFacade = Depends(get_sql_auth_facade)
):
    return RegisterUserUseCase(
        auth_facade
    )
    
async def get_get_user_uc(
    user_repo : UserRepository = Depends(get_sql_user_repo),
    uow : UnitOfWork = Depends(get_sql_unit_of_work)
):
    return GetUserInfoUseCase(
        user_repo,
        uow
    )