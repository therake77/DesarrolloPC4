

from alerts.domain.alert_event_dispatcher import AlertNewMissingPetEvent
from alerts.domain.alert_handler import AlertHandler
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from shared.infrastructure.adapters.sql_uow import SQLUnitOfWork
from users.domain.user_notification import UserNotification
from users.infrastructure.adapters.sql_user_repository import SQLUserRepository

class SQLNewMissinPetHandler(AlertHandler):

    session_factory : async_sessionmaker[AsyncSession]

    def __init__(
            self,
            session_factory : async_sessionmaker[AsyncSession]
        ) -> None:
        super().__init__()
        self.session_factory = session_factory


    async def handle(self, alert : AlertNewMissingPetEvent) -> None:
        async with self.session_factory() as session:
            uow = SQLUnitOfWork(session)
            user_repo = SQLUserRepository(session)
            async with uow:
                all_users = await user_repo.find_all()
                for user in all_users:
                    await user_repo.save_notification(
                        UserNotification(
                            user.uid,
                            alert.alert_id.uid,
                            text=f"Se reportó a una mascota perdida en lat: {alert.coords.lat} long: {alert.coords.long}"
                        )
                    )