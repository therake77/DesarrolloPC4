from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from shared.infrastructure.persistence.base.di import get_async_sql_session
from users.infrastructure.adapters.jwt_token_handler import JwtTokenHandler

from .sql_user_repository import SQLUserRepository


async def get_sql_user_repo(
    session : AsyncSession = Depends(get_async_sql_session)
):
    return SQLUserRepository(
        session
    )

async def get_jwt_token_handler():
    return JwtTokenHandler()