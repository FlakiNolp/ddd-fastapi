import pytest

from app.domain.models.card import Card
from app.domain.models.notification import Notification
from app.domain.models.subscription_plan import SubscriptionPlan
from app.domain.models.user import User
from app.domain.values.card_number import CardNumber
from app.domain.values.cvv import CVV
from app.domain.values.email import Email
from app.domain.values.first_name import FirstName
from app.domain.values.last_name import LastName
from app.domain.values.password import Password
from app.domain.models.project import Project
from app.domain.values.project_name import ProjectName


def test_create_empty_user():
    email = Email('mx@gmail.com')
    password = Password('h.G4aj')
    user = User(email, password)

    assert user.email == email
    assert user.password == password
    assert user.notification.email == user.email
    assert user.projects == set()
    assert user.card == set()
    assert user.subscription_plan == SubscriptionPlan(name='free', event_volume=5000, project_volume=3, data_retention=30)


def test_create_full_user():
    email = Email('mx@gmail.com')
    password = Password('h.G4aj')
    notification = Notification(email, 123, 'osetr')
    projects = {Project(name=ProjectName('first')), Project(name=ProjectName('second'))}
    card = {Card(cart_number=CardNumber('4563714481766217'), owner_last_name=LastName('MAXIM'),
                 owner_first_name=FirstName('OSETROV'), cvv=CVV(543))}
    subscription_plan = SubscriptionPlan(name='first', event_volume=10000, project_volume=5, data_retention=60)
    user = User(email, password, notification=notification, projects=projects, card=card, subscription_plan=subscription_plan)

    assert user.email == email
    assert user.password == password
    assert user.notification == notification
    assert user.projects == projects
    assert user.card == card
    assert user.subscription_plan == subscription_plan


def test_add_to_project():
    email = Email('mx@gmail.com')
    password = Password('h.G4aj')
    user = User(email, password)
    project = Project(name=ProjectName('first'))
    user.add_to_project(project)

    assert project in user.projects