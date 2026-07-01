from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from shared.application.uow import UnitOfWork
from shared.domain.auth_guard import AuthGuard
from shared.infrastructure.adapters.jwt_auth_guard import JWTAuthGuard
from users.domain.token import EncryptedToken
from users.domain.token_handler import TokenHandler
from users.domain.user_repository import UserRepository
from users.infrastructure.adapters.di import get_jwt_token_handler, get_sql_user_repo
from .sql_uow import SQLUnitOfWork
from ..persistence.base.di import get_async_sql_session

async def get_sql_unit_of_work(
    session : AsyncSession = Depends(get_async_sql_session)
):
    return SQLUnitOfWork(
        session
    )

def get_jwt_auth_guard(
    uow  : UnitOfWork = Depends(get_sql_unit_of_work),
    token_handler : TokenHandler = Depends(get_jwt_token_handler),
    user_repo : UserRepository = Depends(get_sql_user_repo)
):
    return JWTAuthGuard(
        token_handler,user_repo, uow
    )

BEARER = HTTPBearer()

async def jwt_auth_guard(
    credentials : HTTPAuthorizationCredentials = Security(BEARER),
    guard : AuthGuard = Depends(get_jwt_auth_guard)
):
    try:
        user =  await guard.resolve_token(EncryptedToken(credentials.credentials))
        print(user)
        return user
    except Exception as e:
        print(e.__str__())
        raise HTTPException(
            status_code=401,    #Unauthorized
            detail="Invalid token or user"
        )