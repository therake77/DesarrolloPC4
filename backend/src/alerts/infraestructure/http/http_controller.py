

from fastapi import APIRouter, Depends, HTTPException

from alerts.application.create_alert import CreateAlertUseCase
from alerts.infraestructure.http.di import get_create_alert_use_case
from alerts.infraestructure.http.dto.missing_pet import MissingPetDto
from shared.domain.coords import Coords
from shared.domain.image import Image
from shared.domain.pet import PetBreed
from shared.infrastructure.adapters.di import jwt_auth_guard
from users.domain.user import User


router = APIRouter(prefix= "/alerts", tags=["alerts"])

@router.post("/")
async def post_missing_pet(
    body : MissingPetDto, 
    user : User = Depends(jwt_auth_guard),
    use_case : CreateAlertUseCase = Depends(get_create_alert_use_case)
):
    print("Executing user case")
    try:
        await use_case.execute(
            body.name,
            Coords(body.lat,body.long),
            body.specie,
            PetBreed(body.breed),
            Image(body.image),
            body.description,
            user.uid.uid
        )
    except Exception as e:
        print(e.__str__())
        raise HTTPException(
            status_code=422,
            detail="Impossible to create"
        )
