from dataclasses import dataclass

from app.domain.values.base import BaseValueObject
from app.domain.exceptions.cvv import CVVValidationException


@dataclass(frozen=True)
class CVV(BaseValueObject):
    value: int

    def validate(self):
        if not (100 <= self.value <= 999):
            raise CVVValidationException(self.value)

    def as_generic_type(self) -> int:
        return self.value
