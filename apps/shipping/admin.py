from django.contrib import admin

from .models import ShippingType, DeliveryNote

admin.site.register(ShippingType)


@admin.register(DeliveryNote)
class DeliveryNoteAdmin(admin.ModelAdmin):
    list_display = ("order", "shipping_type")
