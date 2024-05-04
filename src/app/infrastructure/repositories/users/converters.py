from dataclasses import dataclass

from app.domain.models.user import User


@dataclass
class UserConverter:
    @classmethod
    def convert_model_to_sqlalchemy_user(cls, user: User) -> dict:
        return {
            'oid': user.oid,
            'email': user.email.as_generic_type(),
            'password': user.password.as_generic_type()
        }
