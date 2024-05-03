from punq import Container, Scope

from app.infrastructure.repositories.users import BaseUserRepository, MemoryUserRepository
from app.logic import _init_container


def init_dumpy_container() -> Container:
    container = _init_container()
    container.register(BaseUserRepository, MemoryUserRepository, scope=Scope.singleton)
    return container
