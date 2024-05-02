from dataclasses import dataclass

from app.domain.values.base import BaseValueObject
from app.domain.exceptions.project_name import ProjectNameTooLongException


@dataclass(frozen=True)
class ProjectName(BaseValueObject):
    value: str

    def validate(self):
        if len(self.value) > 150 or len(self.value) < 3:
            raise ProjectNameTooLongException(self.value)

    def as_generic_type(self) -> str:
        return self.value
