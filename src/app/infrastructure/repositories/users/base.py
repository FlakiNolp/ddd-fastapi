import abc
from dataclasses import dataclass

from app.domain.models.user import User


@dataclass
class BaseUserRepository(abc.ABC):
    @abc.abstractmethod
    async def check_user_exists_by_email(self, email: str) -> bool:
        ...

    @abc.abstractmethod
    async def add_user(self, user: User) -> None:
        ...