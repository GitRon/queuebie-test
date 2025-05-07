from queuebie import message_registry
from queuebie.messages import Command

from apps.order.messages.commands.order import CancelOrder
from apps.payment.messages.events.transaction import PaymentTransactionFailed


@message_registry.register_event(event=PaymentTransactionFailed)
def handle_payment_transaction_creation_failed(
    *, context: PaymentTransactionFailed
) -> Command:
    return CancelOrder(
        order=context.order,
    )
