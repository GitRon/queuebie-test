from django.db import models


class ShippingType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class DeliveryNote(models.Model):
    shipping_type = models.ForeignKey(ShippingType, on_delete=models.CASCADE)
    cart = models.ForeignKey("shopping_cart.ShoppingCart", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"#{self.id}"
