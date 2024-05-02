import datetime
from dataclasses import dataclass, field

from app.domain.models.base import BaseModel
from app.domain.models.card import Card
from app.domain.models.notification import Notification
from app.domain.models.project import Project
from app.domain.models.subscription_plan import SubscriptionPlan
from app.domain.values.email import Email
from app.domain.values.password import Password
from app.domain.events.users import NewUserInProject, NewUserCreated


@dataclass
class User(BaseModel):
    email: Email
    password: Password
    projects: set[Project] = field(default_factory=set[Project], kw_only=True)
    card: set[Card] = field(default_factory=set[Card], kw_only=True)
    notification: Notification = field(default=None, kw_only=True)
    subscription_plan: SubscriptionPlan = field(
        default_factory=lambda: SubscriptionPlan(name='free',
                                                 event_volume=5000, project_volume=3,
                                                 data_retention=30), kw_only=True)

    def __hash__(self) -> int:
        return hash(self.oid)

    @classmethod
    def create_user(cls, email: Email, password: Password) -> 'User':
        new_user = cls(email=email, password=password)
        new_user.register_event(NewUserCreated(email=email.as_generic_type(), password=password.as_generic_type()))
        return new_user

    def __post_init__(self):
        if self.notification is None:
            self.notification = Notification(email=self.email)

    def add_to_project(self, project: Project):
        self.projects.add(project)
        self.register_event(NewUserInProject(project_name=project.name.value, project_oid=project.oid, user_oid=self.oid))
