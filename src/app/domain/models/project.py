from dataclasses import dataclass

from app.domain.models.base import BaseModel
from app.domain.values.project_name import ProjectName


@dataclass(match_args=False)
class Project(BaseModel):
    name: ProjectName

    def __hash__(self) -> int:
        return hash(self.oid)
