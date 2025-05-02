from django.urls import path

from apps.product import views

app_name = "team"

urlpatterns = [
    path("shopping-cart/", views.shopping_cart, name="shopping-cart-view"),
]
