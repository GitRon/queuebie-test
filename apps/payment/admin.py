from django.contrib import admin

from .models import PaymentMethod, PaymentTransaction

admin.site.register(PaymentMethod)


@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ("cart", "amount", "payment_method")
