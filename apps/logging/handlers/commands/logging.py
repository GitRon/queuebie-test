import logging

from queuebie import message_registry
from queuebie.messages import Event

from apps.logging.messages.commands.logging import CreateLogEntry
from apps.logging.messages.events.logging import LogEntryCreated


@message_registry.register_command(command=CreateLogEntry)
def handle_create_log_entry(*, context: CreateLogEntry) -> Event:
    logging.getLogger("queuebie-test")

    logging.log(level=context.level, msg=context.message)

    return LogEntryCreated(level=context.level, message=context.message)
