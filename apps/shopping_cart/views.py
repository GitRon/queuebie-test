from django.http import HttpResponse
from django.shortcuts import render
from queuebie.runner import handle_message

from apps.order.messages.commands.order import CreateOrder
from apps.order.models import Order
from apps.order.services import OrderService
from apps.payment.models import PaymentMethod
from apps.product.models import Product


def shopping_cart(request) -> HttpResponse:  # noqa: PBR001
    cart = Order.objects.all().order_by("-id").first()
    return render(
        request=request,
        template_name="shopping_cart/shopping_cart.html",
        context={"object": cart},
    )


def buy_cart_via_imperative_programming(request) -> HttpResponse:  # noqa: PBR001
    service = OrderService(products=Product.objects.all())
    service.process()

    return render(
        request=request,
        template_name="shopping_cart/success.html",
    )


def buy_cart_via_queuebie(request) -> HttpResponse:  # noqa: PBR001
    # Start queue and process messages
    handle_message(
        messages=[
            CreateOrder(
                # Hack to avoid having to implement a product selection in the frontend
                products=Product.objects.all(),
                # Hack to avoid having to implement a payment selection in the frontend
                payment_method=PaymentMethod.objects.all().first(),
            ),
        ]
    )

    return render(
        request=request,
        template_name="shopping_cart/success.html",
    )
