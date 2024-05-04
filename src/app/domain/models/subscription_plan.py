from dataclasses import dataclass, field
import datetime
from typing import Any, Iterable

from app.domain.models.base import BaseModel
from app.domain.values.base import BaseValueObject


@dataclass
class SubscriptionPlan(BaseModel):
    name: str
    payment_date: datetime.date = field(default_factory=datetime.date.today, kw_only=True)
    event_volume: int
    project_volume: int
    data_retention: int

    def __hash__(self) -> int:
        return hash(self.oid)

    def __dict__(self) -> dict:

        def to_dict_recursive(obj: Any) -> Any:
            if isinstance(obj, BaseValueObject):
                return obj.as_generic_type()
            elif isinstance(obj, BaseModel):
                return {key: to_dict_recursive(value) for key, value in obj.__dict__().items()}
            elif isinstance(obj, set):
                return [to_dict_recursive(item) for item in obj]
            elif isinstance(obj, Iterable) and not isinstance(obj, str):
                return [to_dict_recursive(item) for item in obj]
            else:
                return obj

        return {key: to_dict_recursive(value) for key, value in super().__dict__.items()}

    def __eq__(self, __values: 'SubscriptionPlan') -> bool:
        return self.payment_date == self.payment_date and self.event_volume == self.event_volume and self.project_volume == self.project_volume and self.data_retention == self.data_retention
