from dataclasses import dataclass
import email_validator

from app.domain.values.base import BaseValueObject
from app.domain.exceptions.email import EmailValidationException


@dataclass(frozen=True)
class Email(BaseValueObject):
    value: str

    def validate(self):
        try:
            email_validator.validate_email(self.value)
        except email_validator.EmailNotValidError:
            raise EmailValidationException(text=self.value)

    def as_generic_type(self) -> str:
        return self.value

