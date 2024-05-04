from punq import Container
from pytest import fixture

from app.infrastructure.repositories.users.base import BaseUserRepository
from app.logic.mediator import Mediator
from app.tests.fixtues import init_dumpy_container


@fixture(scope='function')
def container() -> Container:
    return init_dumpy_container()


@fixture(scope='function')
def mediator(container: Container) -> Mediator:
    return container.resolve(Mediator)


@fixture(scope='function')
def user_repository(container: Container) -> BaseUserRepository:
    return container.resolve(BaseUserRepository)
