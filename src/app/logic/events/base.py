import abc
from dataclasses import dataclass
from typing import Any

from app.domain.events.base import BaseEvent


@dataclass
class EventHandler[ET: BaseEvent, ER: Any](abc.ABC):
    def handle(self, event: ET) -> ER:
        ...
