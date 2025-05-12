from factory.django import DjangoModelFactory

from apps.order.models import Order


class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order
