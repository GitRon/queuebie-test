from factory.django import DjangoModelFactory

from apps.payment.models import PaymentMethod


class PaymentMethodFactory(DjangoModelFactory):
    class Meta:
        model = PaymentMethod
