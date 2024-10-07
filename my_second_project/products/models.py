from django.db import models

class Product(models.Model):
    article_name = models.TextField(max_length=50, verbose_name = "nombre",null=True)
    color = models.TextField(max_length=50, verbose_name = "color",null=True)
    price = models.TextField(max_length=10, verbose_name = "precio",null=True)
    size = models.TextField(max_length=50, verbose_name = "talla",null=True)
    photo = models.ImageField(upload_to="logos", height_field=None, width_field=None, max_length=None, null=True, blank=True, verbose_name="foto")

    def __str__(self):
        return self.article_name    