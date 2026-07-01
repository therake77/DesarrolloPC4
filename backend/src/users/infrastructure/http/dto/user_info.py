

from pydantic import BaseModel


class UserInfoDto(BaseModel):
    id : int
    name : str
    email : str