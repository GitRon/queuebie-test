from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from apps.shopping_cart.models import ShoppingCart


def shopping_cart(request) -> HttpResponse:  # noqa: PBR001
    cart = ShoppingCart.objects.all().order_by("-id").first()
    return render(
        request=request,
        template_name="shopping_cart/shopping_cart.html",
        context={"object": cart},
    )


def buy_cart(request, pk: int) -> HttpResponse:  # noqa: PBR001
    cart = get_object_or_404(ShoppingCart, pk=pk)

    # todo: hier wirds spannend

    return render(
        request=request,
        template_name="shopping_cart/success.html",
        context={"object": cart},
    )
