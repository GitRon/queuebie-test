from dataclasses import dataclass

from django.db.models import QuerySet
from queuebie.messages import Command

from apps.order.models import Order
from apps.product.models import Product


@dataclass(kw_only=True)
class CreateOrder(Command):
    products: QuerySet[Product]


@dataclass(kw_only=True)
class CancelOrder(Command):
    order: Order


@dataclass(kw_only=True)
class ConfirmOrder(Command):
    order: Order
