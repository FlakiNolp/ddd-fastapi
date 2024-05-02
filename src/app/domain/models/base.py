import uuid
from dataclasses import dataclass, field

from app.domain.events.base import BaseEvent


@dataclass()
class BaseModel:
    oid: uuid.UUID = field(default_factory=lambda: uuid.uuid4(), kw_only=True)
    __events: list[BaseEvent] = field(
        default_factory=list,
        kw_only=True
    )

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, __value: 'BaseModel') -> bool:
        return self.oid == __value.oid

    def __ne__(self, __value: 'BaseModel') -> bool:
        return self.oid != __value.oid

    def register_event(self, event: BaseEvent) -> None:
        self.__events.append(event)

    def pull_events(self) -> list[BaseEvent]:
        registered_events = self.__events.copy()
        self.__events.clear()
        return registered_events
