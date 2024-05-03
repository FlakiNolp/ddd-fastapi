from functools import lru_cache

from punq import Container, Scope

from app.logic.commands.users import CreateUserCommand, CreateUserCommandHandler
from app.logic.mediator import Mediator
from app.infrastructure.repositories.users import MemoryUserRepository, BaseUserRepository


@lru_cache(1)
def init_container():
    return _init_container()


def _init_container() -> Container:
    container = Container()
    container.register(BaseUserRepository, MemoryUserRepository, scope=Scope.singleton)
    container.register(CreateUserCommandHandler)

    def init_mediator():
        mediator = Mediator()
        mediator.register_command(
            CreateUserCommand,
            [container.resolve(service_key=CreateUserCommandHandler)]
        )
        return mediator

    container.register(Mediator, factory=init_mediator)
    return container
