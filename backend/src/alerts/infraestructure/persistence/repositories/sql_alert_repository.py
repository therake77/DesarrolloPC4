

from sqlalchemy import delete, select, update

from alerts.domain.alert import Alert, AlertId
from alerts.domain.alert_repository import AlertRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from alerts.infraestructure.persistence.models.alert import AlertModel
from shared.domain.coords import Coords
from shared.domain.image import Image
from shared.domain.pet import Pet, PetBreed
from users.domain.user import HashedPassword, User, UserCredentials, UserEmail, UserId, UserName
from users.infrastructure.persistence.user import UserModel

class SQLAlertRepository(AlertRepository):

    session : AsyncSession

    def __init__(
            self,
            session : AsyncSession
        ) -> None:
        super().__init__()
        self.session = session

    async def get_by_id( self, id : AlertId) -> Alert | None:
        result = (
            await self.session.execute(
            select(AlertModel)
            .where(AlertModel.id == id.uid)
            .options(selectinload(AlertModel.user))
        )).scalar_one_or_none()
        if result is None: return None
        user = (
            await self.session.execute(
                select(UserModel)
                .where(UserModel.id == result.user_id)
                .options(selectinload(UserModel.credential))
            )
        ).scalar_one_or_none()
        if user is None: return None
        return Alert(
            AlertId(result.id),
            Coords(result.lat,result.long),
            Image(result.image),
            User(
                UserId(user.id),
                    UserName(user.name),
                    user.role,
                    UserCredentials(
                        UserEmail(user.credential.email),
                        HashedPassword(user.credential.password)
                    )
            ),
            Pet(
                result.pet_name,
                result.pet_specie,
                PetBreed(result.pet_breed)
            ),
            result.description
        )
    
    async def save_alert( self, alert : Alert) -> AlertId:
        new_model = AlertModel(
                lat = alert.location.lat,
                long = alert.location.long,
                image = alert.image.image_repr,
                user_id = alert.user.uid.uid ,
                pet_name = alert.pet.name ,
                pet_specie = alert.pet.specie, 
                pet_breed = alert.pet.breed.breed_name,
                description = alert.description
            )
        self.session.add(
            new_model
        )
        await self.session.flush()
        return AlertId(new_model.id)
    
    async def update_alert(self, alert: Alert) -> None:
        await self.session.execute(
            update(AlertModel)
            .where(AlertModel.id == alert.id.uid)
            .values(
                lat = alert.location.lat,
                long = alert.location.long,
                image = alert.image.image_repr,
                user_id = alert.user.uid ,
                pet_name = alert.pet.name ,
                pet_specie = alert.pet.specie, 
                pet_breed = alert.pet.breed,
                description = alert.description
            )
        )
        await self.session.flush()
        return

    async def delete_alert(self, alert: Alert) -> None:
        await self.session.execute(
            delete(AlertModel)
            .where(AlertModel.id == alert.id.uid)
        )
        await self.session.flush()
        return
   