from dataclasses import dataclass

from users.domain.user import UserId


@dataclass
class UserNotification:
    user_id : UserId
    alert_id : int
    text : str