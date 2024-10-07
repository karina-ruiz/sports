from django.views import generic
from .models import Product

class ProductListView(generic.ListView):
    model = Product
    template_name = "product/add_product.html"
    context_object_name = "products"

    