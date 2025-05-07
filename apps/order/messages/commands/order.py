from dataclasses import dataclass

from django.db.models import QuerySet
from queuebie.messages import Command

from apps.order.models import Order
from apps.payment.models import PaymentMethod
from apps.product.models import Product


@dataclass(kw_only=True)
class CreateOrder(Command):
    products: QuerySet[Product]
    payment_method: PaymentMethod


@dataclass(kw_only=True)
class CancelOrder(Command):
    order: Order


@dataclass(kw_only=True)
class ConfirmOrder(Command):
    order: Order


@dataclass(kw_only=True)
class FinishOrder(Command):
    order: Order
