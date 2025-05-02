from apps.payment.models import PaymentTransaction
from apps.shipping.models import DeliveryNote
from apps.shopping_cart.models import ShoppingCart


class ShoppingCartService:
    cart: ShoppingCart

    def __init__(self, cart: ShoppingCart):
        super().__init__()

        self.cart = cart

    def process(self):
        payment_method = self.cart.payment_method
        payment_transaction, _ = PaymentTransaction.objects.get_or_create(
            payment_method=payment_method, cart=self.cart
        )

        shipping_type = self.cart.shipping_type
        delivery_note, _ = DeliveryNote.objects.get_or_create(
            shipping_type=shipping_type, cart=self.cart
        )

        self.cart.status = ShoppingCart.StatusChoices.SUCCESS
        self.cart.save()
