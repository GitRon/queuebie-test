import pytest

from apps.order.handlers.commands.order import (
    handle_create_order,
    handle_cancel_order,
    handle_confirm_order,
    handle_finish_order,
)
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
from apps.order.tests.factories.order import ProductFactory
from apps.payment.tests.factories.payment_method import PaymentMethodFactory
from apps.product.models import Product
from apps.product.tests.factories.product import OrderFactory


@pytest.mark.django_db
def test_handle_create_order_regular():
    products = Product.objects.filter(
        pk__in=[p.id for p in ProductFactory.create_batch(size=2)]
    )
    context = CreateOrder(products=products, payment_method=PaymentMethodFactory())

    event = handle_create_order(context=context)

    assert isinstance(event, OrderCreated)
    assert isinstance(event.order, Order)

    assert list(event.order.products.values_list("id", flat=True)) == list(
        products.values_list("id", flat=True)
    )


@pytest.mark.django_db
def test_handle_cancel_order_regular():
    order = OrderFactory()
    context = CancelOrder(order=order)

    event = handle_cancel_order(context=context)

    assert isinstance(event, OrderCancelled)
    assert event.order == order
    assert event.order.status == Order.StatusChoices.CANCELLED


@pytest.mark.django_db
def test_handle_confirm_order_regular():
    order = OrderFactory()
    context = ConfirmOrder(order=order)

    event = handle_confirm_order(context=context)

    assert isinstance(event, OrderConfirmed)
    assert event.order == order
    assert event.order.status == Order.StatusChoices.CONFIRMED


@pytest.mark.django_db
def test_handle_finish_order_regular():
    order = OrderFactory()
    context = FinishOrder(order=order)

    event = handle_finish_order(context=context)

    assert isinstance(event, OrderFinished)
    assert event.order == order
    assert event.order.status == Order.StatusChoices.SUCCESS
