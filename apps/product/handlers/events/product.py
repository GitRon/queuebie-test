from queuebie import message_registry
from queuebie.messages import Command

from apps.order.messages.events.order import OrderCreated
from apps.product.messages.commands.product import CalculatePrice


@message_registry.register_event(event=OrderCreated)
def handle_create_price_for_new_order(*, context: OrderCreated) -> Command:
    return CalculatePrice(
        order=context.order,
    )
