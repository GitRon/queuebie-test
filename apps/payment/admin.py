from django.contrib import admin

from .models import PaymentMethod, PaymentTransaction

admin.site.register(PaymentMethod)
admin.site.register(PaymentTransaction)
