from django.contrib.auth.models import User
from django.db import models
    
class Product(models.Model):
    name = models.TextField(max_length=100, verbose_name="nombre", null=True)
    photo = models.ImageField(upload_to="logos", null=True, blank=True, verbose_name="foto")
    brand = models.TextField(max_length=100, verbose_name="marca", null=True, blank=True)
    code = models.TextField(max_length=100, verbose_name="codigo", null=True)
    detail = models.TextField(max_length=500, verbose_name="descripcion", null=True)
    categoria =  models.TextField(max_length=100, verbose_name="categoria", null=True)
    size =  models.TextField(max_length=100, verbose_name="talla", null=True)
    color =  models.TextField(max_length=100, verbose_name="color", null=True)
    price = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="precio", null=True)
    unit_cost = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="costo_unitario", null=True)
    available = models.BooleanField(default="True", verbose_name="disponible", null=True)

    def __str__(self):
        return self.name if self.name else "Producto sin nombre"

class Inventario(models.Model):
    initial_amount = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    entradas = models.IntegerField(null="True")
    salidas = models.IntegerField(null="True")
    stock_actual = models.IntegerField(null="True")