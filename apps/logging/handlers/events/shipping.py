import logging

from queuebie import message_registry
from queuebie.messages import Command

from apps.logging.messages.commands.logging import CreateLogEntry
from apps.shipping.messages.events.delivery_note import DeliveryNoteCreated


@message_registry.register_event(event=DeliveryNoteCreated)
def handle_log_delivery_note_created(*, context: DeliveryNoteCreated) -> Command:
    return CreateLogEntry(
        message=f"Created delivery note #{context.delivery_note} for order #{context.delivery_note.order.id}.",
        level=logging.INFO,
    )
