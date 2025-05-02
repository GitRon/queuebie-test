from django.http import HttpResponse
from django.shortcuts import render


def shopping_cart(request) -> HttpResponse:  # noqa: PBR001
    return render(request=request, template_name="product/shopping_cart.html")
