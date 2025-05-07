from django.db.models import Sum
from queuebie import message_registry
from queuebie.messages import Event

from apps.product.messages.commands.product import CalculatePrice
from apps.product.messages.events.product import PriceCalculated


@message_registry.register_command(command=CalculatePrice)
def handle_calculate_price(*, context: CalculatePrice) -> Event:
    total_price = context.order.products.all().aggregate(total=Sum("price"))["total"]

    return PriceCalculated(order=context.order, total_price=total_price)
