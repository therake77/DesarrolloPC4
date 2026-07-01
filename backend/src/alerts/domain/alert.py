from dataclasses import dataclass
from shared.domain.coords import Coords
from shared.domain.image import Image
from users.domain.user import User


@dataclass
class Alert:
    location : Coords
    image : Image
    issuer : User