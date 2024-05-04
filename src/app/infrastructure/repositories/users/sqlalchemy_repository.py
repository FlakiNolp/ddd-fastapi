from dataclasses import dataclass
from sqlalchemy import select, Sequence
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine, AsyncEngine

from app.domain.models.user import User as DomainUser
from app.infrastructure.models.user import User as SQLAlchemyUser
from app.infrastructure.repositories.users.base import BaseUserRepository
from app.infrastructure.repositories.users.converters import UserConverter


@dataclass
class SQLAlchemyUserRepository(BaseUserRepository):
    uri: str

    def __post_init__(self):
        self.__async_engine: AsyncEngine = create_async_engine(url=self.uri)
        self.__session_maker = async_sessionmaker(self.__async_engine, expire_on_commit=False)

    async def check_user_exists_by_email(self, email: str) -> bool:
        async with self.__session_maker() as async_session:
            res = (await async_session.scalars(select(SQLAlchemyUser).filter(SQLAlchemyUser.email == email))).one_or_none()
            if res is None:
                return False
            return True

    async def add_user(self, user: DomainUser):
        async with self.__session_maker() as async_session:
            async_session.add(SQLAlchemyUser(**UserConverter.convert_model_to_sqlalchemy_user(user)))
            await async_session.commit()
