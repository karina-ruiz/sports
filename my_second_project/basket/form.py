from django import forms
from .models import Payment

class PaymentForm(forms.Form):
    name_cart = forms.CharField(label='Nombre de Tarjeta', max_length=50)
    card_number = forms.DecimalField(label='Número de Tarjeta', max_digits=16, decimal_places=0)
    expiry_month = forms.DecimalField(label='Mes de Expiración', max_digits=2, decimal_places=0)
    expiry_year = forms.DecimalField(label='Año de Expiración', max_digits=4, decimal_places=0)
    cvv = forms.DecimalField(label='CVV', max_digits=4, decimal_places=0, widget=forms.TextInput(attrs={'placeholder': 'CVV'}))

    def save(self):
        Payment.objects.create(
            name_cart=self.cleaned_data["name_cart"],
            card_number=self.cleaned_data["card_number"],
            expiry_month=self.cleaned_data["expiry_month"],
            expiry_year=self.cleaned_data["expiry_year"],
            cvv=self.cleaned_data["cvv"],
        )
