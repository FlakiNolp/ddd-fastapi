from dataclasses import dataclass
from typing import Any

from app.domain.models.user import User
from app.domain.values.email import Email
from app.domain.values.password import Password
from app.infrastructure.repositories.users import BaseUserRepository
from app.logic.commands.base import BaseCommand, CommandHandler
from app.logic.exceptions.users import UserWithThatEmailAlreadyExistsException


@dataclass(frozen=True)
class CreateUserCommand(BaseCommand):
    email: str
    password: str


@dataclass(frozen=True)
class CreateUserCommandHandler(CommandHandler[CreateUserCommand, User]):
    user_repository: BaseUserRepository

    async def handle(self, command: CreateUserCommand) -> User:
        if await self.user_repository.check_user_exists_by_email(email=command.email):
            raise UserWithThatEmailAlreadyExistsException(command.email)
        new_user = User.create_user(email=Email(value=command.email), password=Password(command.password))
        await self.user_repository.add_user(new_user)
        return new_user

