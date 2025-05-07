from queuebie import message_registry
from queuebie.messages import Command

from apps.shipping.messages.commands.delivery_note import CreateDeliveryNote
from apps.shipping.messages.events.delivery_note import ShippingTypeDecided
from apps.shipping.models import DeliveryNote


@message_registry.register_event(event=ShippingTypeDecided)
def handle_shipping_type_decided(*, context: ShippingTypeDecided) -> Command | None:
    if context.shipping_type == DeliveryNote.ShippingTypeChoices.FREIGHT:
        return CreateDeliveryNote(
            shipping_type=DeliveryNote.ShippingTypeChoices.FREIGHT,
            order=context.order,
            # Shipping price is a fixed rate for the truck to deliver the products
            shipping_price=DeliveryNote.FREIGHT_SHIPPING_COST,
        )
    elif context.shipping_type == DeliveryNote.ShippingTypeChoices.POSTAL:
        return CreateDeliveryNote(
            shipping_type=DeliveryNote.ShippingTypeChoices.POSTAL,
            order=context.order,
            # Shipping price is determined by the number of shipped items
            shipping_price=context.no_of_products * 3,
        )
    return None
