from django.db import models


class DeliveryNote(models.Model):
    class ShippingTypeChoices(models.IntegerChoices):
        POSTAL = 1, "Postal service"
        FREIGHT = 2, "Freight forwarding"

    FREIGHT_SHIPPING_COST = 249

    shipping_type = models.PositiveSmallIntegerField(choices=ShippingTypeChoices)
    order = models.ForeignKey("order.Order", on_delete=models.CASCADE)
    shipping_price = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"#{self.id}"
