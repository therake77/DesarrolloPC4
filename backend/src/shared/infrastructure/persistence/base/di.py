
from shared.infrastructure.persistence.base.base import async_session_factory

async def get_async_sql_session():
    async with async_session_factory() as session:
        yield session