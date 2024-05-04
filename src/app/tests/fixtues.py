from punq import Container, Scope

from app.infrastructure.repositories.users.base import BaseUserRepository
from app.infrastructure.repositories.users.sqlalchemy_repository import SQLAlchemyUserRepository
from app.logic import _init_container


def init_dumpy_container() -> Container:
    container = _init_container()
    container.register(BaseUserRepository, SQLAlchemyUserRepository, scope=Scope.singleton)
    return container
