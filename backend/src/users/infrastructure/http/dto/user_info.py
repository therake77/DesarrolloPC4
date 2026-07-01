

from pydantic import BaseModel

from users.domain.user import UserRole


class UserInfoDto(BaseModel):
    id : int
    name : str
    email : str
    role : UserRole