
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship 
from shared.infrastructure.persistence.models.base_model import BaseSQLAlchemyModel


class UserModel(BaseSQLAlchemyModel):

    __tablename__ = "user"

    name : Mapped[str] = mapped_column( String(length=255))
    credential : Mapped["UserCredentialsModel"] = relationship(back_populates="user")

class UserCredentialsModel(BaseSQLAlchemyModel):

    __tablename__ = "user_credential"

    user_id : Mapped[int] = mapped_column(ForeignKey("user.id"))
    email : Mapped[str] = mapped_column(String(255))
    password : Mapped[str] = mapped_column(String(255))

    user : Mapped["UserModel"] = relationship(back_populates="credential") 