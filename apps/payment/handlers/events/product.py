from queuebie import message_registry
from queuebie.messages import Command

from apps.payment.messages.commands.transaction import CreatePaymentTransaction
from apps.product.messages.events.product import PriceCalculated


@message_registry.register_event(event=PriceCalculated)
def handle_price_calculated(*, context: PriceCalculated) -> Command:
    return CreatePaymentTransaction(
        order=context.order,
        amount=context.total_price,
        payment_method=context.order.payment_method,
    )
