from dataclasses import dataclass

from users.domain.user import UserId


@dataclass
class Token:
    user_id : UserId


@dataclass
class EncryptedToken:
    as_raw : str