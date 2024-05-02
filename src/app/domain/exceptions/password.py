from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class PasswordValidationException(ApplicationException):
    text: str

    @property
    def message(self) -> str:
        return f'Пароль должен содержать {self.text}'
    
