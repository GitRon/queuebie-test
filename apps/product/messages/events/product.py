from dataclasses import dataclass

from queuebie.messages import Event

from apps.order.models import Order


@dataclass(kw_only=True)
class PriceCalculated(Event):
    order: Order
    total_price: int
