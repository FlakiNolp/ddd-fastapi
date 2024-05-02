from dataclasses import dataclass

from app.logic.exceptions.base import LogicException


@dataclass(frozen=True, eq=False)
class ProjectVolumeIsEndedException(LogicException):
    name: str

    @property
    def message(self):
        return f'Лимит проектов изчерапн. Если хотите создать больше - требуется повысить тариф <{self.name}>'