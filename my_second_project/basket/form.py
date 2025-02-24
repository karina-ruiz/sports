from django import forms

class PaymentForm(forms.Form):
    name_cart = forms.CharField(label='Nombre de Tarjeta', max_length=50)
    card_number =  forms.CharField(label='Número de Tarjeta', max_length=50)
    expiry_month = forms.CharField(label='Mes de Expiración', max_length=2)
    expiry_year = forms.CharField(label='Año de Expiración', max_length=4)
    cvv = forms.CharField(label='CVV', max_length=4, widget=forms.TextInput(attrs={'placeholder': 'CVV'}))


    