from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .sql_uow import SQLUnitOfWork
from ..persistence.base.di import get_async_sql_session

async def get_sql_unit_of_work(
    session : AsyncSession = Depends(get_async_sql_session)
):
    return SQLUnitOfWork(
        session
    )