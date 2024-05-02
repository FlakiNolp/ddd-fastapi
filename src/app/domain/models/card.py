from dataclasses import dataclass

from app.domain.models.base import BaseModel
from app.domain.values.card_number import CardNumber
from app.domain.values.cvv import CVV
from app.domain.values.first_name import FirstName
from app.domain.values.last_name import LastName


@dataclass
class Card(BaseModel):
    cart_number: CardNumber
    owner_first_name: FirstName
    owner_last_name: LastName
    cvv: CVV

    def __hash__(self) -> int:
        return hash(self.oid)
