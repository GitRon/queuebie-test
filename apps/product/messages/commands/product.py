from dataclasses import dataclass

from queuebie.messages import Command

from apps.order.models import Order


@dataclass(kw_only=True)
class CalculatePrice(Command):
    order: Order
