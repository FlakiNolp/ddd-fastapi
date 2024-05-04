from functools import lru_cache

from punq import Container, Scope

from app.logic.commands.users import CreateUserCommand, CreateUserCommandHandler
from app.logic.mediator import Mediator
from app.infrastructure.repositories.users.base import BaseUserRepository
from app.infrastructure.repositories.users.sqlalchemy_repository import SQLAlchemyUserRepository
from app.settings.config import Config


@lru_cache(1)
def init_container():
    return _init_container()


def _init_container() -> Container:
    container = Container()
    container.register(CreateUserCommandHandler)
    container.register(Config, instance=Config(), scope=Scope.singleton)

    def init_mediator():
        mediator = Mediator()
        mediator.register_command(
            CreateUserCommand,
            [container.resolve(service_key=CreateUserCommandHandler)]
        )
        return mediator

    def init_user_sqlalchemy_repository():
        config: Config = container.resolve(Config)
        return SQLAlchemyUserRepository(config.postgres_connection_uri)

    container.register(BaseUserRepository, factory=init_user_sqlalchemy_repository, scope=Scope.singleton)
    init_user_sqlalchemy_repository()
    container.register(Mediator, factory=init_mediator)
    return container
