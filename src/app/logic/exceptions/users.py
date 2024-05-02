from dataclasses import dataclass

from app.logic.exceptions.base import LogicException


@dataclass(frozen=True, eq=False)
class UserWithThatEmailAlreadyExistsException(LogicException):
    email: str

    @property
    def message(self):
        return f'Пользователь с такой почтой <{self.email}> уже сущесвует'
