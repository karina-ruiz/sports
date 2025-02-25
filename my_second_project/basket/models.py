from django.db import models

# Create your models here.
class Payment (models.Model):
    name_cart = models.CharField(verbose_name='Nombre de Tarjeta', max_length=50)
    card_number =  models.DecimalField(verbose_name='Número de Tarjeta',max_digits=10, decimal_places=0)
    expiry_month = models.DecimalField(verbose_name='Mes de Expiración', max_digits=2, decimal_places=0)
    expiry_year = models.DecimalField(verbose_name='Año de Expiración', max_digits=4, decimal_places=0)
    cvv = models.DecimalField(verbose_name='CVV', max_digits=4, decimal_places=0)