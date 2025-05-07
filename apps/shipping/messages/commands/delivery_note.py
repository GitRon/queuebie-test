from dataclasses import dataclass

from queuebie.messages import Command

from apps.order.models import Order


@dataclass(kw_only=True)
class DecideOnShippingTypes(Command):
    order: Order


@dataclass(kw_only=True)
class CreateDeliveryNote(Command):
    order: Order
    shipping_price: int
    shipping_type: int
