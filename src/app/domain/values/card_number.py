from dataclasses import dataclass
import re

from app.domain.values.base import BaseValueObject
from app.domain.exceptions.card_number import CardNumberValidationException


@dataclass(frozen=True)
class CardNumber(BaseValueObject):
    value: str

    def validate(self):
        if re.match(
            r'^(?:4[0-9]{12}(?:[0-9]{3})?|[25][1-7][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$',
            self.value
        ) is None:
            raise CardNumberValidationException(self.value)

    def as_generic_type(self) -> str:
        return self.value
