from dataclasses import dataclass

from queuebie.messages import Event

from apps.order.models import Order
from apps.payment.models import PaymentTransaction


@dataclass(kw_only=True)
class PaymentTransactionCreated(Event):
    payment_transaction: PaymentTransaction


@dataclass(kw_only=True)
class PaymentTransactionFailed(Event):
    order: Order
    reason: str
