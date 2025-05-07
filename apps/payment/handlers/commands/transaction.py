import random

from queuebie import message_registry
from queuebie.messages import Event

from apps.payment.exceptions import PaymentTransactionException
from apps.payment.messages.commands.transaction import CreatePaymentTransaction
from apps.payment.messages.events.transaction import (
    PaymentTransactionCreated,
    PaymentTransactionFailed,
)
from apps.payment.models import PaymentTransaction


@message_registry.register_command(command=CreatePaymentTransaction)
def handle_create_payment_transaction(*, context: CreatePaymentTransaction) -> Event:
    try:
        # Pretending to have some external force which might cause a transaction verification to fail
        if random.random() < 0.2:
            raise PaymentTransactionException("Transaction couldn't be confirmed.")
        transaction = PaymentTransaction.objects.create(
            payment_method=context.order.payment_method,
            amount=context.amount,
            order=context.order,
        )

        return PaymentTransactionCreated(payment_transaction=transaction)

    except PaymentTransactionException as e:
        return PaymentTransactionFailed(order=context.order, reason=str(e))
