

from pydantic import BaseModel


class NotificationDto(BaseModel):
    alert_id : int
    text : str