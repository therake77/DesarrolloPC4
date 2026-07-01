
from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship 
from shared.infrastructure.persistence.models.base_model import BaseSQLAlchemyModel
from users.domain.user import UserRole
if TYPE_CHECKING:
    from alerts.infraestructure.persistence.models.alert import AlertModel

class UserModel(BaseSQLAlchemyModel):

    __tablename__ = "user"

    name : Mapped[str] = mapped_column( String(length=255))
    credential : Mapped["UserCredentialsModel"] = relationship(back_populates="user")
    role : Mapped[UserRole] = mapped_column(default=UserRole.SOLIDARIO)
    alerts : Mapped[List["AlertModel"]] = relationship(back_populates="user")
    notifications : Mapped[List["UserNotificationModel"]] = relationship(back_populates="user")

class UserCredentialsModel(BaseSQLAlchemyModel):

    __tablename__ = "user_credential"

    user_id : Mapped[int] = mapped_column(ForeignKey("user.id"))
    email : Mapped[str] = mapped_column(String(255))
    password : Mapped[str] = mapped_column(String(255))

    user : Mapped["UserModel"] = relationship(back_populates="credential") 

class UserNotificationModel(BaseSQLAlchemyModel):
    __tablename__ = "user_notification"

    user_id : Mapped[int] = mapped_column(ForeignKey("user.id"))
    alert_id : Mapped[int] = mapped_column(ForeignKey("alert.id"))
    text : Mapped[str] = mapped_column(String(255))

    user : Mapped["UserModel"] = relationship(back_populates="notifications")
    alert : Mapped["AlertModel"] = relationship(back_populates="notification")