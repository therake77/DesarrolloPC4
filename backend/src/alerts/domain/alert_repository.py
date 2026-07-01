

from abc import ABC, abstractmethod

from alerts.domain.alert import Alert, AlertId


class AlertRepository(ABC):

    @abstractmethod
    async def get_by_id( self, id : AlertId) -> Alert | None:
        pass

    @abstractmethod
    async def save_alert( self, alert : Alert) -> AlertId:
        pass

    @abstractmethod
    async def update_alert(self, alert: Alert) -> None:
        pass

    @abstractmethod
    async def delete_alert(self, alert: Alert) -> None:
        pass