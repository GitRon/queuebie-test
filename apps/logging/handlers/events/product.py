import logging

from queuebie import message_registry
from queuebie.messages import Command

from apps.logging.messages.commands.logging import CreateLogEntry
from apps.product.messages.events.product import PriceCalculated


@message_registry.register_event(event=PriceCalculated)
def handle_log_price_calculated(*, context: PriceCalculated) -> Command:
    return CreateLogEntry(
        message=f"Calculated price {context.total_price}€ for order #{context.order.id}.",
        level=logging.INFO,
    )
