from dataclasses import dataclass
import re

from app.domain.exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class CVVValidationException(ApplicationException):
    text: int

    @property
    def message(self) -> str:
        return f'Ошибка валидации cvv <{self.text}>'
