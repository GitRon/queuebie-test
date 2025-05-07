import logging

from queuebie import message_registry
from queuebie.messages import Command

from apps.logging.messages.commands.logging import CreateLogEntry
from apps.order.messages.events.order import OrderCreated, OrderCancelled


@message_registry.register_event(event=OrderCreated)
def handle_log_order_created(*, context: OrderCreated) -> Command:
    return CreateLogEntry(
        message=f"Order #{context.order.id} created", level=logging.INFO
    )


@message_registry.register_event(event=OrderCancelled)
def handle_log_order_cancelled(*, context: OrderCancelled) -> Command:
    return CreateLogEntry(
        message=f"Order #{context.order.id} was cancelled", level=logging.WARNING
    )
