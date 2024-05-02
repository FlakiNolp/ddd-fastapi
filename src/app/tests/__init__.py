from app.logic.commands.users import CreateUserCommand, CreateUserCommandHandler
from app.logic.mediator import Mediator
from app.infrastructure.repositories.users import MemoryUserRepository, BaseUserRepository


def init_mediator(
        mediator: Mediator,
        user_repository: BaseUserRepository,
):
    mediator.register_command(
        CreateUserCommand,
        [CreateUserCommandHandler(user_repository=user_repository)]
    )