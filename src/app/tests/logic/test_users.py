from app.domain.values.email import Email
from app.domain.values.password import Password
from app.tests.conftest import *  #noqa
import pytest

from app.domain.models.user import User
from app.infrastructure.repositories.users import BaseUserRepository
from app.logic import Mediator, CreateUserCommand
from app.logic.exceptions.users import UserWithThatEmailAlreadyExistsException


@pytest.mark.asyncio
async def test_created_user_command_success(
    user_repository: BaseUserRepository,
    mediator: Mediator,
):
    user: User
    user, *_ = await mediator.handle_command(CreateUserCommand(email='a@gmail.com', password='aB6.12321'))
    assert await user_repository.check_user_exists_by_email(email=user.email.as_generic_type())


@pytest.mark.asyncio
async def test_created_user_command_email_already_exists(
    user_repository: BaseUserRepository,
    mediator: Mediator,
):
    user: User = User(email=Email('a@gmail.com'), password=Password('aB6.12321'))
    await user_repository.add_user(user)

    assert user in user_repository._saved_users

    with pytest.raises(UserWithThatEmailAlreadyExistsException):
        await mediator.handle_command(CreateUserCommand(email='a@gmail.com', password='aB6.12321'))

    assert len(user_repository._saved_users) == 1