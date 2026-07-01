
from ...application.uow import UnitOfWork
from sqlalchemy.ext.asyncio import AsyncSession

class SQLUnitOfWork(UnitOfWork):

    async_session : AsyncSession

    def __init__(
            self,
            async_session : AsyncSession
        ) -> None:
        super().__init__()
        self.async_session = async_session

    async def begin(self) -> None:
        await self.async_session.begin()
        return

    async def commit(self) -> None:
        await self.async_session.commit()
        return

    async def rollback(self) -> None:
        await self.async_session.rollback()
        return