from django.contrib import admin

from .models import Order
from ..payment.admin import PaymentInline
from ..shipping.admin import DeliveryNoteInline


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [PaymentInline, DeliveryNoteInline]
    list_display = ("id", "payment_method", "status")
