from django.contrib import admin

from .models import PaymentMethod, PaymentTransaction

admin.site.register(PaymentMethod)


class PaymentInline(admin.StackedInline):
    extra = 0
    model = PaymentTransaction


@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = ("order", "amount", "payment_method")
