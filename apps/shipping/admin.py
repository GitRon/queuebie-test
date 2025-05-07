from django.contrib import admin

from .models import DeliveryNote


class DeliveryNoteInline(admin.StackedInline):
    extra = 0
    model = DeliveryNote


@admin.register(DeliveryNote)
class DeliveryNoteAdmin(admin.ModelAdmin):
    list_display = ("order", "shipping_type")
