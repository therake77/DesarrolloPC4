
from pydantic import BaseModel


class RegisterDto(BaseModel):
    name : str
    email : str
    password : str