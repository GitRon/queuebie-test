from dataclasses import dataclass

from queuebie.messages import Command

from apps.order.models import Order
from apps.payment.models import PaymentMethod


@dataclass(kw_only=True)
class CreatePaymentTransaction(Command):
    order: Order
    payment_method: PaymentMethod
    amount: int
