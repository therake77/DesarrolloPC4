
from dataclasses import dataclass
from enum import Enum

 
class UserRole(Enum):
    SOLIDARIO = "SOLIDARIO"
    PROFESIONAL = "PROFESIONAL"
    ESPECIALIZADO = "ESPECIALIZADO"

@dataclass
class UserEmail:
    email : str

@dataclass
class HashedPassword:
    as_raw : str

@dataclass
class UserCredentials:
    email : UserEmail
    hashed_password : HashedPassword

@dataclass
class UserId:
    uid : int

@dataclass
class UserName:
    name : str

@dataclass
class User:
    uid : UserId
    name : UserName
    role : UserRole
    credentials : UserCredentials


@dataclass
class Caretaker(User):
    level : str