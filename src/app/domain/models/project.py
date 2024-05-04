from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any

from app.domain.models.base import BaseModel
from app.domain.values.base import BaseValueObject
from app.domain.values.project_name import ProjectName


@dataclass
class Project(BaseModel):
    name: ProjectName

    def __hash__(self) -> int:
        return hash(self.oid)

    def __dict__(self) -> dict:

        def to_dict_recursive(obj: Any) -> Any:
            if isinstance(obj, BaseValueObject):
                return obj.as_generic_type()
            elif isinstance(obj, BaseModel):
                return {key: to_dict_recursive(value) for key, value in obj.__dict__().items()}
            elif isinstance(obj, set):
                return [to_dict_recursive(item) for item in obj]
            elif isinstance(obj, Iterable) and not isinstance(obj, str):
                return [to_dict_recursive(item) for item in obj]
            else:
                return obj

        return {key: to_dict_recursive(value) for key, value in super().__dict__.items()}


if __name__ == '__main__':
    project = Project(name=ProjectName('test'))
    print(project.__dict__())
