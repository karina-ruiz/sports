from django.contrib.auth.models import User
from django.db import models
class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    article_name = models.TextField(max_length=50, verbose_name = "nombre",null=True)
    price = models.TextField(max_length=10, verbose_name = "precio",null=True)
    detail = models.TextField(max_length=300, null=True)
    photo = models.ImageField(null=True, blank=True, verbose_name="foto") 
    sizes = models.ManyToManyField(Size)
    colors = models.ManyToManyField(Color)


    def __str__(self):
        return self.article_name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('Product', through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
