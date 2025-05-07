from dataclasses import dataclass

from queuebie.messages import Event

from apps.order.models import Order
from apps.shipping.models import DeliveryNote


@dataclass(kw_only=True)
class ShippingTypeDecided(Event):
    order: Order
    shipping_type: int
    no_of_products: int


@dataclass(kw_only=True)
class DeliveryNoteCreated(Event):
    delivery_note: DeliveryNote
