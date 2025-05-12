import pytest
from django.http import HttpResponse
from django.test import RequestFactory

from apps.order.models import Order
from apps.order.tests.factories.order import ProductFactory
from apps.payment.tests.factories.payment_method import PaymentMethodFactory
from apps.shopping_cart.views import buy_cart_via_queuebie


@pytest.mark.django_db
def test_buy_cart_via_queuebie_status_code():
    # Create required objects
    PaymentMethodFactory()
    ProductFactory()

    # Call view
    request = RequestFactory().get("/")
    response = buy_cart_via_queuebie(request=request)

    # Assert response
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200


@pytest.mark.django_db
def test_integration_buy_cart_via_queuebie_order_created_with_status_success():
    # Create required objects
    payment_method = PaymentMethodFactory()
    product = ProductFactory()

    # Call view
    request = RequestFactory().get("/")
    buy_cart_via_queuebie(request=request)

    created_orders = Order.objects.filter(
        payment_method=payment_method, products__in=[product]
    )

    assert created_orders.count() == 1

    order = created_orders.first()
    assert order.status == Order.StatusChoices.SUCCESS
