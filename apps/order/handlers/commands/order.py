from queuebie import message_registry
from queuebie.messages import Event

from apps.order.messages.commands.order import (
    CreateOrder,
    CancelOrder,
    ConfirmOrder,
    FinishOrder,
)
from apps.order.messages.events.order import (
    OrderCreated,
    OrderCancelled,
    OrderConfirmed,
    OrderFinished,
)
from apps.order.models import Order


@message_registry.register_command(command=CreateOrder)
def handle_create_order(*, context: CreateOrder) -> Event:
    order = Order.objects.create(payment_method=context.payment_method)
    order.products.set(context.products.all())

    return OrderCreated(order=order)


@message_registry.register_command(command=CancelOrder)
def handle_cancel_order(*, context: CancelOrder) -> Event:
    context.order.status = Order.StatusChoices.CANCELLED
    context.order.save()

    return OrderCancelled(order=context.order)


@message_registry.register_command(command=ConfirmOrder)
def handle_confirm_order(*, context: ConfirmOrder) -> Event:
    context.order.status = Order.StatusChoices.CONFIRMED
    context.order.save()

    return OrderConfirmed(order=context.order)


@message_registry.register_command(command=FinishOrder)
def handle_finish_order(*, context: FinishOrder) -> Event:
    context.order.status = Order.StatusChoices.SUCCESS
    context.order.save()

    return OrderFinished(order=context.order)
