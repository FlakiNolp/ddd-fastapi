from fastapi import status, Depends
from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException

from app.application.api.schemas import ErrorSchema
from app.application.api.users.schemas import CreateUserRequestSchema, CreateUserResponseSchema
from app.domain.exceptions.base import ApplicationException
from app.logic import init_container
from app.logic.commands.users import CreateUserCommand
from app.logic.mediator import Mediator

router = APIRouter(
    tags=["app"]
)


@router.post(
    '/',
    response_model=CreateUserResponseSchema,
    status_code=status.HTTP_201_CREATED,
    description='Создает нового пользователя, если пользователя с таким email не существует',
    responses={
        status.HTTP_201_CREATED: {'model': CreateUserResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema},
    }
)
async def create_chat_handler(schema: CreateUserRequestSchema, container=Depends(init_container)):
    mediator: Mediator = container.resolve(Mediator)
    try:
        user, *_ = await mediator.handle_command(CreateUserCommand(email=schema.email, password=schema.password))
    except ApplicationException as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})
    return CreateUserResponseSchema.from_model(user)
