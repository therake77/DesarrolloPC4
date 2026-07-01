

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from alerts.infraestructure.persistence.repositories.sql_alert_repository import SQLAlertRepository
from shared.infrastructure.persistence.base.di import get_async_sql_session


def get_sql_alert_repository(
    session : AsyncSession = Depends(get_async_sql_session)
):
    return SQLAlertRepository(
        session
    )