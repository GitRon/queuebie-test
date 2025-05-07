from django.db import models

from apps.payment.models import PaymentMethod
from apps.product.models import Product


class Order(models.Model):
    class StatusChoices(models.IntegerChoices):
        PENDING = 1, "Pending"
        CONFIRMED = 2, "Confirmed"
        SUCCESS = 3, "Success"
        CANCELLED = 4, "Cancelled"

    products = models.ManyToManyField(Product, blank=True)
    payment_method = models.ForeignKey(
        PaymentMethod, blank=True, null=True, on_delete=models.CASCADE
    )
    status = models.PositiveSmallIntegerField(
        choices=StatusChoices.choices, default=StatusChoices.PENDING
    )

    def __str__(self) -> str:
        return f"#{self.id}"
