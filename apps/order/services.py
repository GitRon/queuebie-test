import logging
import random
from logging import Logger

from django.db.models import QuerySet, Sum

from apps.order.models import Order
from apps.payment.exceptions import PaymentTransactionException
from apps.payment.models import PaymentTransaction, PaymentMethod
from apps.product.models import Product
from apps.shipping.models import DeliveryNote


class OrderService:
    order: Order
    logger: Logger

    def __init__(
        self, *, payment_method: PaymentMethod, products: QuerySet[Product]
    ) -> None:
        super().__init__()

        self.order = Order.objects.create(
            products=products,
            payment_method=payment_method,
        )
        self.logger = logging.getLogger("order")

    def process(self) -> None:
        # Calculate price
        total_price = self.order.products.aggregate(total=Sum("price"))["total"]
        self.logger.info(f"Total price: {total_price}")

        # Create payment transaction
        try:
            # Pretending to have some external force which might cause a transaction verification to fail
            if random.random() < 0.2:
                raise PaymentTransactionException("Transaction couldn't be confirmed.")
            PaymentTransaction.objects.create(
                payment_method=self.order.payment_method,
                amount=total_price,
                order=self.order,
            )

            self.order.status = Order.StatusChoices.CONFIRMED
            self.order.save()
            self.logger.info("Order confirmed.")
        except PaymentTransactionException:
            self.order.status = Order.StatusChoices.CANCELLED
            self.order.save()
            self.logger.info("Order cancelled.")
            return

        # Handle shipping
        bulky_products = self.order.products.filter(is_bulky=True)
        regular_products = self.order.products.filter(is_bulky=False)

        if bulky_products.exists():
            DeliveryNote.objects.create(
                shipping_type=DeliveryNote.ShippingTypeChoices.FREIGHT,
                order=self.order,
                # Shipping price is a fixed rate for the truck to deliver the products
                shipping_price=DeliveryNote.FREIGHT_SHIPPING_COST,
            )
            self.logger.info("Order delivery note for freight forwarding created.")
        elif regular_products.exists():
            DeliveryNote.objects.create(
                shipping_type=DeliveryNote.ShippingTypeChoices.POSTAL,
                order=self.order,
                # Shipping price is determined by the number of shipped items
                shipping_price=regular_products.count() * 3,
            )
            self.logger.info("Order delivery note for postal services created.")

        # Mark the order as successful
        self.order.status = Order.StatusChoices.SUCCESS
        self.order.save()
        self.logger.info("Order successful.")
