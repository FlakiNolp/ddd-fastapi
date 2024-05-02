from pytest import fixture

from app.infrastructure.repositories.users import BaseUserRepository, MemoryUserRepository
from app.tests import Mediator, init_mediator


@fixture(scope='function')
def user_repository() -> MemoryUserRepository:
    return MemoryUserRepository()


@fixture(scope='function')
def mediator(user_repository: BaseUserRepository) -> Mediator:
    mediator = Mediator()
    init_mediator(mediator, user_repository)
    return mediator
