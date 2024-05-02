from dataclasses import dataclass
import re

from app.domain.values.base import BaseValueObject
from app.domain.exceptions.first_name import FirstNameValidationException


@dataclass(frozen=True)
class FirstName(BaseValueObject):
    value: str

    def validate(self):
        if len(self.value) > 150 or re.search(r"^[A-Z]+$", self.value) is None:
            raise FirstNameValidationException(self.value)

    def as_generic_type(self) -> str:
        return self.value

