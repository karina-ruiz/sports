from django.contrib import admin
from .models import Product, Size, Color

class ProductAdmin(admin.ModelAdmin):
    list_display = ('article_name', 'price', 'detail', 'photo', 'get_sizes', 'get_colors')

    def get_sizes(self, obj):
        return ", ".join([size.name for size in obj.sizes.all()])
    get_sizes.short_description = 'Tallas'  

    def get_colors(self, obj):
        return ", ".join([color.name for color in obj.colors.all()])
    get_colors.short_description = 'Colores'  

admin.site.register(Product, ProductAdmin)
admin.site.register(Size)
admin.site.register(Color)