

from abc import ABC, abstractmethod


class UnitOfWork(ABC):

    async def __aenter__(self):
        await self.begin()
        return self

    async def __aexit__(self, exc_type, exc, tb):#type: ignore
        if exc_type:
            try:
                await self.rollback()
            except Exception as e3:
                raise RollbackException("Cannot rollback") from e3
        else:
            try:
                await self.commit()
            except Exception as e1:
                try:
                    await self.rollback()
                except Exception as e2:
                    raise RollbackException("Cannot rollback") from e2
                raise CommitException("Cannot commit") from e1

    @abstractmethod
    async def begin(self) -> None:
        pass

    @abstractmethod
    async def commit(self) -> None:
        pass

    @abstractmethod
    async def rollback(self) -> None:
        pass

class RollbackException(Exception): pass
class CommitException(Exception): pass