from queuebie import message_registry
from queuebie.messages import Command

from apps.order.messages.events.order import OrderConfirmed
from apps.shipping.messages.commands.delivery_note import DecideOnShippingTypes


@message_registry.register_event(event=OrderConfirmed)
def handle_order_confirmed(*, context: OrderConfirmed) -> Command | None:
    return DecideOnShippingTypes(order=context.order)
