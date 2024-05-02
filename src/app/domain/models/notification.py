from dataclasses import dataclass, field

from app.domain.models.base import BaseModel
from app.domain.values.email import Email


@dataclass
class Notification(BaseModel):
    email: Email
    telegram_id: int = field(default=None)
    vk_domain: str = field(default=None)

    def __hash__(self) -> int:
        return hash(self.oid)
