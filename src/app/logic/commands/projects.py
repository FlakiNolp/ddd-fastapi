from dataclasses import dataclass
from typing import Any

from app.domain.models.project import Project
from app.infrastructure.repositories.subscription_plans import BaseSubscriptionPlan
from app.logic.commands.base import BaseCommand, CommandHandler


@dataclass(frozen=True)
class CreateProjectCommand(BaseCommand):
    name: str


@dataclass(frozen=True)
class CreateProjectCommandHandler(CommandHandler[CreateProjectCommand]):
    subscription_plan: BaseSubscriptionPlanRepository

    async def handle(self, command: CreateProjectCommand) -> Project:
        if self.subscription_plan.project_volume_is_not_end is None:
            raise ProjectVolumeIsEndedException(command.name)
