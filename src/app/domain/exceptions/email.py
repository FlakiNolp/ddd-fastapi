from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class EmailValidationException(ApplicationException):
    text: str

    @property
    def message(self) -> str:
        return f'Ошибка валидации почтового адреса <{self.text}>'
