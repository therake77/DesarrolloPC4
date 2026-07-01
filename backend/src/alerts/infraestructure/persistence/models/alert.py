from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, String

from shared.domain.pet import PetSpecie
from shared.infrastructure.persistence.models.base_model import BaseSQLAlchemyModel
from sqlalchemy.orm import MappedColumn, mapped_column, Mapped, relationship
if TYPE_CHECKING:
    from users.infrastructure.persistence.user import UserModel
    from users.infrastructure.persistence.user import UserNotificationModel

class AlertModel(BaseSQLAlchemyModel):
    
    __tablename__ = "alert"

    lat : MappedColumn[float] = mapped_column(Float)
    long  : MappedColumn[float] = mapped_column(Float)
    image : MappedColumn[str] = mapped_column(String(255))
    user_id : MappedColumn[int] = mapped_column(ForeignKey("user.id"))

    pet_name : MappedColumn[str] = mapped_column(String(255))
    pet_specie : MappedColumn[PetSpecie] = mapped_column(default=PetSpecie.CAT)
    pet_breed : MappedColumn[str] = mapped_column(String(255))

    description : MappedColumn[str] = mapped_column(String(255))

    user : Mapped["UserModel"] = relationship(back_populates="alerts")
    notification : Mapped["UserNotificationModel"] = relationship(back_populates="alert")