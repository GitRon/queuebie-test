from factory.django import DjangoModelFactory

from apps.product.models import Product


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product
