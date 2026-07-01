

from fastapi import Depends, Request

from alerts.application.create_alert import CreateAlertUseCase
from alerts.domain.alert_repository import AlertRepository
from alerts.infraestructure.persistence.di import get_sql_alert_repository
from shared.application.uow import UnitOfWork
from shared.infrastructure.adapters.di import get_sql_unit_of_work
from users.domain.user_repository import UserRepository
from users.infrastructure.adapters.di import get_sql_user_repo


def get_create_alert_use_case(
    request : Request,
    alert_repository : AlertRepository = Depends(get_sql_alert_repository),
    user_repository : UserRepository = Depends(get_sql_user_repo),
    uow : UnitOfWork = Depends(get_sql_unit_of_work)
):
    return CreateAlertUseCase(
        alert_repository,
        user_repository,
        uow,
        request.app.state.alert_event_dispatcher
    )