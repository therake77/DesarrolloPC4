

from pydantic import BaseModel

from shared.domain.pet import PetSpecie


class MissingPetDto(BaseModel):
    name : str
    specie : PetSpecie
    breed: str
    image : str
    description : str
    long : float
    lat : float