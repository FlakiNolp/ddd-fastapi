from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class ProjectNameTooLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f'Название проекта слишком длинное <{self.text[:150]}...>'

