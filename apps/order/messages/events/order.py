from dataclasses import dataclass

from queuebie.messages import Event

from apps.order.models import Order


@dataclass(kw_only=True)
class OrderCreated(Event):
    order: Order


@dataclass(kw_only=True)
class OrderCancelled(Event):
    order: Order


@dataclass(kw_only=True)
class OrderConfirmed(Event):
    order: Order
