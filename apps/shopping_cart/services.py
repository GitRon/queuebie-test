from django.db.models import Sum

from apps.payment.models import PaymentTransaction
from apps.shipping.models import DeliveryNote
from apps.shopping_cart.models import ShoppingCart


class ShoppingCartService:
    cart: ShoppingCart

    def __init__(self, *, cart: ShoppingCart):
        super().__init__()

        self.cart = cart

    def process(self):
        total_price = self.cart.products.aggregate(total=Sum("price"))["total"]

        payment_method = self.cart.payment_method
        PaymentTransaction.objects.create(
            payment_method=payment_method, amount=total_price, cart=self.cart
        )

        shipping_type = self.cart.shipping_type
        DeliveryNote.objects.create(shipping_type=shipping_type, cart=self.cart)

        self.cart.status = ShoppingCart.StatusChoices.SUCCESS
        self.cart.save()
