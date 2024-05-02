from dataclasses import dataclass, field
import datetime

from app.domain.models.base import BaseModel


@dataclass
class SubscriptionPlan(BaseModel):
    name: str
    payment_date: datetime.date = field(default_factory=datetime.date.today, kw_only=True)
    event_volume: int
    project_volume: int
    data_retention: int

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, __values: 'SubscriptionPlan') -> bool:
        return self.payment_date == self.payment_date and self.event_volume == self.event_volume and self.project_volume == self.project_volume and self.data_retention == self.data_retention
