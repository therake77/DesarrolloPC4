from dataclasses import dataclass
from shared.domain.pet import Pet
from shared.domain.coords import Coords
from shared.domain.image import Image
from users.domain.user import User

@dataclass
class AlertId:
    uid : int

@dataclass
class Alert:
    id : AlertId
    location : Coords
    image : Image
    user : User
    pet : Pet
    description : str