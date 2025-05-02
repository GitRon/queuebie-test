from django.db import models

from apps.payment.models import PaymentMethod
from apps.product.models import Product
from apps.shipping.models import ShippingType


class ShoppingCart(models.Model):
    class StatusChoices(models.IntegerChoices):
        PENDING = 1, "Pending"
        SUCCESS = 2, "Bought"
        EXPIRED = 3, "Expired"

    products = models.ManyToManyField(Product, blank=True)
    payment_method = models.ForeignKey(
        PaymentMethod, blank=True, null=True, on_delete=models.CASCADE
    )
    shipping_type = models.ForeignKey(
        ShippingType, blank=True, null=True, on_delete=models.CASCADE
    )
    status = models.PositiveSmallIntegerField(
        choices=StatusChoices.choices, default=StatusChoices.PENDING
    )

    def __str__(self) -> str:
        return f"#{self.id}"
