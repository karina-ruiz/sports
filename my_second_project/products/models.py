from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
    
class Categoria(models.Model):
    nombre = models.TextField(null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.descripcion}"
class Product(models.Model):
    name = models.TextField(verbose_name="nombre", null=True)
    photo = models.ImageField(upload_to="logos", null=True, blank=True, verbose_name="foto")
    brand = models.TextField(verbose_name="marca", null=True, blank=True)
    code = models.TextField(verbose_name="codigo", null=True)
    detail = models.TextField(verbose_name="descripcion", null=True)
    size =  models.TextField(verbose_name="talla", null=True)
    color =  models.TextField(verbose_name="color", null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="precio", null=True)
    unit_cost = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="costo_unitario", null=True)
    available = models.BooleanField(default="True", verbose_name="disponible", null=True)
    categoria = models.ForeignKey(Categoria, related_name='productos', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else "Producto sin nombre"

class Order(models.Model):  
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    telephone_number = models.CharField(max_length=15)
    email = models.EmailField()
    created_id = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="pending")

    def __str__(self):
        return f"Order {self.id} by {self.full_name}"
    
class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  
    quantity = models.PositiveIntegerField() 

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'