
from pydantic import BaseModel

from users.domain.user import UserRole


class RegisterDto(BaseModel):
    name : str
    email : str
    password : str
    role : UserRole