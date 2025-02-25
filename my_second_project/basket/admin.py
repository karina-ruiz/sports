from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name_cart', 'cvv', 'card_number', 'expiry_month', 'expiry_year')
    # Puedes agregar más configuraciones según sea necesario
