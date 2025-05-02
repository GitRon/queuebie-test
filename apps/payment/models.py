from django.db import models


class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class PaymentTransaction(models.Model):
    amount = models.PositiveSmallIntegerField()
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    cart = models.ForeignKey("shopping_cart.ShoppingCart", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"#{self.id}"
