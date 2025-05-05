from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from apps.order.models import Order
from apps.order.services import OrderService


def shopping_cart(request) -> HttpResponse:  # noqa: PBR001
    cart = Order.objects.all().order_by("-id").first()
    return render(
        request=request,
        template_name="shopping_cart/shopping_cart.html",
        context={"object": cart},
    )


def buy_cart_via_imperative_programming(request, pk: int) -> HttpResponse:  # noqa: PBR001
    order = get_object_or_404(Order, pk=pk)

    service = OrderService(order=order)
    service.process()

    return render(
        request=request,
        template_name="shopping_cart/success.html",
    )
