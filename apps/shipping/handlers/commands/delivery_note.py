from queuebie import message_registry
from queuebie.messages import Event

from apps.shipping.messages.commands.delivery_note import (
    CreateDeliveryNote,
    DecideOnShippingTypes,
)
from apps.shipping.messages.events.delivery_note import (
    DeliveryNoteCreated,
    ShippingTypeDecided,
)
from apps.shipping.models import DeliveryNote


@message_registry.register_command(command=DecideOnShippingTypes)
def handle_decide_on_shipping_types(*, context: DecideOnShippingTypes) -> list[Event]:
    # Handle shipping
    bulky_products = context.order.products.filter(is_bulky=True)
    regular_products = context.order.products.filter(is_bulky=False)

    messages = []
    if bulky_products.exists():
        messages.append(
            ShippingTypeDecided(
                shipping_type=DeliveryNote.ShippingTypeChoices.FREIGHT,
                order=context.order,
                no_of_products=bulky_products.count(),
            )
        )
    if regular_products.exists():
        messages.append(
            ShippingTypeDecided(
                shipping_type=DeliveryNote.ShippingTypeChoices.POSTAL,
                order=context.order,
                no_of_products=regular_products.count(),
            )
        )
    return messages


@message_registry.register_command(command=CreateDeliveryNote)
def handle_create_delivery_note(*, context: CreateDeliveryNote) -> Event:
    delivery_note = DeliveryNote.objects.create(
        shipping_type=context.shipping_type,
        order=context.order,
        shipping_price=context.shipping_price,
    )

    return DeliveryNoteCreated(delivery_note=delivery_note)
