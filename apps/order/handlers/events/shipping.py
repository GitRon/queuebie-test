from queuebie import message_registry
from queuebie.messages import Command

from apps.order.messages.commands.order import FinishOrder
from apps.shipping.messages.events.delivery_note import DeliveryNoteCreated


@message_registry.register_event(event=DeliveryNoteCreated)
def handle_payment_transaction_creation_failed(
    *, context: DeliveryNoteCreated
) -> Command:
    return FinishOrder(order=context.delivery_note.order)
