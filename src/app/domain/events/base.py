import abc
import uuid
from dataclasses import dataclass, field


@dataclass
class BaseEvent(abc.ABC):
    event_id: uuid.UUID = field(default_factory=lambda: uuid.uuid4(), kw_only=True)
