from django.urls import path

from apps.shopping_cart import views

app_name = "team"

urlpatterns = [
    path("shopping-cart/buy/<int:pk>", views.buy_cart, name="shopping-cart-buy-view"),
    path("shopping-cart/", views.shopping_cart, name="shopping-cart-view"),
]
