from dataclasses import dataclass, field

from app.domain.models.user import User
from app.infrastructure.repositories.users.base import BaseUserRepository


@dataclass
class MemoryUserRepository(BaseUserRepository):
    _saved_users: list[User] = field(default_factory=list, kw_only=True)

    async def check_user_exists_by_email(self, email: str) -> bool:
        try:
            return bool(next(filter(lambda user: user.email.as_generic_type() == email, self._saved_users)))
        except StopIteration:
            return False

    async def add_user(self, user: User) -> None:
        self._saved_users.append(user)

