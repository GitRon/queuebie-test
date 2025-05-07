from queuebie import message_registry
from queuebie.messages import Command

from apps.order.messages.commands.order import CancelOrder, ConfirmOrder
from apps.payment.messages.events.transaction import (
    PaymentTransactionFailed,
    PaymentTransactionCreated,
)


@message_registry.register_event(event=PaymentTransactionFailed)
def handle_payment_transaction_creation_failed(
    *, context: PaymentTransactionFailed
) -> Command:
    return CancelOrder(order=context.order)


@message_registry.register_event(event=PaymentTransactionCreated)
def handle_payment_transaction_creation_successful(
    *, context: PaymentTransactionCreated
) -> Command:
    return ConfirmOrder(order=context.payment_transaction.order)
