from django.urls import path

from apps.shopping_cart import views

app_name = "team"

urlpatterns = [
    path(
        "shopping-cart/buy/imperative/<int:pk>",
        views.buy_cart_via_imperative_programming,
        name="shopping-cart-buy-imperative-view",
    ),
    path("shopping-cart/", views.shopping_cart, name="shopping-cart-view"),
]
