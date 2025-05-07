import logging

from queuebie import message_registry
from queuebie.messages import Command

from apps.logging.messages.commands.logging import CreateLogEntry
from apps.payment.messages.events.transaction import PaymentTransactionFailed


@message_registry.register_event(event=PaymentTransactionFailed)
def handle_log_payment_transaction_failed(
    *, context: PaymentTransactionFailed
) -> Command:
    return CreateLogEntry(
        message=f"Payment transaction failed for order #{context.order.id}.",
        level=logging.ERROR,
    )
