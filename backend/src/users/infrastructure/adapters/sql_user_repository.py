from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select, update
from sqlalchemy.orm import selectinload
from users.domain.user import HashedPassword, User, UserCredentials, UserEmail, UserId, UserName
from users.infrastructure.persistence.user import UserCredentialsModel, UserModel
from users.domain.user_repository import UserRepository


class SQLUserRepository(UserRepository):

    async_session : AsyncSession

    def __init__(
            self,
            async_session : AsyncSession
        ) -> None:
        super().__init__()
        self.async_session = async_session
    
    async def find_by_id( self, id : UserId)->User | None:
        result = (await self.async_session.execute(
            select(UserModel)
            .where( UserModel.id == id.uid)
            .options(
                selectinload(UserModel.credential)
            )
        )).scalar_one_or_none()
        if result is None: return None
        return self._to_domain(result)
    
    async def find_by_email( self, email : UserEmail)-> User | None:
        credential = (
            await self.async_session.execute(
                select(UserCredentialsModel)
                .where(UserCredentialsModel.email == email.email)
                .options(
                    selectinload(UserCredentialsModel.user)
                )
            )
        ).scalar_one_or_none()
        if(credential is None): return None

        return self._to_domain_from_credentials(credential)

    
    async def update_user( self, user : User)->None:
        await self.async_session.execute(
            update(UserModel)
            .where(UserModel.id == user.uid.uid)
            .values(
                name = user.name.name
            )
        )
        await self.async_session.execute(
            update(UserCredentialsModel)
            .where(UserCredentialsModel.user_id == user.uid.uid)
            .values(
                email = user.credentials.email,
                password = user.credentials.hashed_password
            )
        )
        await self.async_session.flush()
        return
    
    async def save_user( self, user : User)->None:
        self.async_session.add(
            UserModel(
                name = user.name.name,
                credential = UserCredentialsModel(
                    email = user.credentials.email.email,
                    password = user.credentials.hashed_password.as_raw
                )
            )
        )
        await self.async_session.flush()
        return

    
    async def delete_user( self, id : UserId)->None:
        await self.async_session.execute(
            delete(UserModel)
            .where(UserModel.id == id.uid)
        )
        await self.async_session.flush()
        return

    
    def _to_domain(self, model : UserModel) -> User:
        return User(
            UserId(model.id),
            UserName(model.name),
            UserCredentials(
                UserEmail(model.credential.email),
                hashed_password=HashedPassword(model.credential.password)
            )
        )
    
    def _to_domain_from_credentials(self, model : UserCredentialsModel) -> User:
        return User(
            UserId(model.user.id),
            UserName(model.user.name),
            UserCredentials(
                UserEmail(model.email),
                hashed_password=HashedPassword(model.password)
            )
        )
    