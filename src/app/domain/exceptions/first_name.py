from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class FirstNameValidationException(ApplicationException):
    text: str

    @property
    def message(self) -> str:
        return f'Ошибка валидации имени <{self.text}>'
