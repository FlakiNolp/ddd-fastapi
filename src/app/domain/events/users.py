import uuid
from dataclasses import dataclass

from app.domain.events.base import BaseEvent
from app.domain.values.project_name import ProjectName


@dataclass
class NewUserInProject(BaseEvent):
    project_name: str
    project_oid: uuid.UUID
    user_oid: uuid.UUID


@dataclass
class NewUserCreated(BaseEvent):
    email: str
    password: str
