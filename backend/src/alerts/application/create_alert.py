from alerts.domain.alert import Alert, AlertId
from alerts.domain.alert_event_dispatcher import AlertNewMissingPetEvent, AlertNewMissingPetSubject
from alerts.domain.alert_repository import AlertRepository
from shared.application.uow import UnitOfWork
from shared.domain.coords import Coords
from shared.domain.image import Image
from shared.domain.pet import Pet, PetBreed, PetSpecie
from users.domain.user import User, UserId
from users.domain.user_repository import UserRepository


class CreateAlertUseCase:

    alert_repo : AlertRepository
    user_repo : UserRepository
    uow : UnitOfWork
    alert_subject : AlertNewMissingPetSubject

    def __init__(
            self,
            alert_repository : AlertRepository,
            user_repository : UserRepository,
            uow : UnitOfWork,
            alert_event_dispatcher : AlertNewMissingPetSubject
        ) -> None:
        self.alert_repo = alert_repository
        self.user_repo = user_repository
        self.uow  = uow
        self.alert_subject = alert_event_dispatcher

    async def execute( 
        self,
        pet_name : str,
        location : Coords,
        pet_specie : PetSpecie,
        pet_breed : PetBreed,
        image : Image,
        description : str,
        issuer : int
     ):
        print("Inside use case")
        async with self.uow :
            user : User | None = await self.user_repo.find_by_id(UserId(issuer))
            print(user)
            if user is None: raise Exception
            id  = await self.alert_repo.save_alert(
                Alert(
                    AlertId(0),
                    location,
                    image,
                    user,
                    Pet(
                        pet_name,
                        pet_specie,
                        pet_breed
                    ),
                    description
                )
            )
            print(id)
        await self.alert_subject.notify(
            AlertNewMissingPetEvent(
                id,
                location
            )
        )