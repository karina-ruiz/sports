from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = [
         "article_name",
         "color",
         "price",
         "size",
         "photo"
    ]
    search_fields = [
        "article_name",
         "color",
         "price",
         "size",
         "photo"
    ]
admin.site.register(Product, ProductAdmin)