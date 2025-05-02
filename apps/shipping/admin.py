from django.contrib import admin

from .models import ShippingType, DeliveryNote

admin.site.register(ShippingType)
admin.site.register(DeliveryNote)
