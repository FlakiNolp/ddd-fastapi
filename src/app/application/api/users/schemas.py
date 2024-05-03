import uuid

from pydantic import BaseModel, EmailStr

from app.domain.models.user import User


class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: str


class CreateUserResponseSchema(BaseModel):
    oid: uuid.UUID
    email: EmailStr

    @classmethod
    def from_model(cls, user: User) -> 'CreateUserResponseSchema':
        return CreateUserResponseSchema(
            oid=user.oid,
            email=user.email.as_generic_type(),
        )