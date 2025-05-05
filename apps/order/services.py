from apps.order.models import Order
from apps.payment.models import PaymentTransaction
from apps.product.services import ProductPricingService
from apps.shipping.services import DeliveryNoteService


class OrderService:
    order: Order

    def __init__(self, *, order: Order):
        super().__init__()

        self.order = order

    def process(self):
        total_price = ProductPricingService().process(
            products=self.order.products.all()
        )

        payment_method = self.order.payment_method
        PaymentTransaction.objects.create(
            payment_method=payment_method, amount=total_price, order=self.order
        )

        shipping_type = self.order.shipping_type
        DeliveryNoteService().process(
            shipping_type=shipping_type,
            quantity=self.order.products.all().count() * 3,
            order=self.order,
        )

        self.order.status = Order.StatusChoices.SUCCESS
        self.order.save()
