from django.db import models


class ShippingType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class DeliveryNote(models.Model):
    SHIPPING_COST = 249
    shipping_type = models.ForeignKey(ShippingType, on_delete=models.CASCADE)
    order = models.ForeignKey("order.Order", on_delete=models.CASCADE)
    shipping_price = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"#{self.id}"
