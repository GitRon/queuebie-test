from django.urls import path

from apps.shopping_cart import views

app_name = "team"

urlpatterns = [
    path(
        "shopping-cart/buy/imperative/",
        views.buy_cart_via_imperative_programming,
        name="shopping-cart-buy-imperative-view",
    ),
    path(
        "shopping-cart/buy/queuebie/",
        views.buy_cart_via_queuebie,
        name="shopping-cart-buy-queuebie-view",
    ),
    path("shopping-cart/", views.shopping_cart, name="shopping-cart-view"),
]
