from dataclasses import dataclass
from enum import Enum

class PetSpecie(Enum):
    DOG = "DOG"
    CAT = "CAT"
    BIRD = "BIRD"

@dataclass
class PetBreed:
    breed_name : str
    
@dataclass
class Pet:
    name : str
    specie : PetSpecie
    breed: PetBreed