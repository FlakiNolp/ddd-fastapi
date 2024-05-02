from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Iterable

from app.domain.events.base import BaseEvent
from app.logic.commands.base import BaseCommand, CommandHandler
from app.logic.events.base import EventHandler
from app.logic.exceptions.mediator import EventHandlersNotRegisteredException, CommandHandlersNotRegisteredException


@dataclass
class Mediator[ET: BaseEvent, ER: Any, CT: BaseCommand, CR: Any]:
    events_map: dict[ET, list[EventHandler]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )
    commands_map: dict[CT, list[CommandHandler]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True
    )

    def register_event(self, event: ET, event_handlers: Iterable[EventHandler[ET, ER]]):
        self.events_map[event].append(event_handlers)

    def register_command(self, command: CT, command_handlers: Iterable[CommandHandler[CT, CR]]):
        self.events_map[command].extend(command_handlers)

    async def handle_event(self, event: ET) -> Iterable[ER]:
        handlers = self.events_map.get(event)
        if not handlers:
            raise EventHandlersNotRegisteredException(event)
        return [await handler.handle(event) for handler in handlers]

    async def handle_command(self, command: BaseCommand) -> Iterable[CR]:
        command_type = command.__class__
        handlers = self.events_map.get(command_type)
        if not handlers:
            raise CommandHandlersNotRegisteredException(command_type)
        return [await handler.handle(command) for handler in handlers]
