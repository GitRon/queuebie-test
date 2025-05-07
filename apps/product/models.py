from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField(default=0)
    is_bulky = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
