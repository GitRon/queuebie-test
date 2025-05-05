from apps.order.models import Order
from apps.shipping.models import ShippingType, DeliveryNote


class DeliveryNoteService:
    def process(
        self, *, order: Order, shipping_type: ShippingType, quantity: int
    ) -> DeliveryNote:
        return DeliveryNote.objects.create(
            shipping_type=shipping_type,
            order=order,
            shipping_price=quantity,
        )
