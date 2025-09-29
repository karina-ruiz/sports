from django.db import models

# Create your models here.
class Payment (models.Model):
    name_cart = models.CharField(verbose_name='Nombre de Tarjeta', max_length=50)
    card_number =  models.DecimalField(verbose_name='Número de Tarjeta',max_digits=10, decimal_places=0)
    expiry_month = models.DecimalField(verbose_name='Mes de Expiración', max_digits=2, decimal_places=0)
    expiry_year = models.DecimalField(verbose_name='Año de Expiración', max_digits=4, decimal_places=0)
    cvv = models.DecimalField(verbose_name='CVV', max_digits=4, decimal_places=0)


class Siena (models.Model):
    tipo_evento_choices = [
        ("desecho", "Desecho"),
        ("salir al jardin", "Salir al jardin"),
        ("entrar al jardin", "Entrar al jardin"),
        ("familia sale de la casa", "Familia sale de la casa"),
        ("familia entra a la casa", "Familia entra a la casa"),
    ]
    lugar_choices = [
        ("cocina", "Cocina"),
        ("sala", "Sala"),
        ("baño", "Baño"),
        ("patio", "Patio"),
        ("dormitorio", "Dormitorio"),
    ]
    actividad_choises = [
        ("pipi", "Pipi"),
        ("popo", "Popo"),
    ]
    tipo_de_evento = models.CharField(max_length=50, choices=tipo_evento_choices, default='desecho')
    fecha = models.DateTimeField(verbose_name="Hora en la que Defeco")
    lugar = models.CharField(max_length=50, choices=lugar_choices, default='patio')
    actividad = models.CharField(max_length=10, choices=actividad_choises, default="popo")
    regaño = models.BooleanField(default=False, verbose_name="regaño")

    def __str__(self):
        return f"{self.hora_Defeca} - {self.get_lugar_display()} - {self.get_actividad_display()}"






class SienaAfuera (models.Model):



class SienaAdentroCuandoSalimos (models.Model):



class SienaRegañada (models.Model):
