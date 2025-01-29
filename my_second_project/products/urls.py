from django.urls import path
from .views import ProductListView, ProductDetailView, buscar_producto


urlpatterns = [
    path("", ProductListView.as_view(), name="list_product"),
    path("buscar/", buscar_producto, name="buscar_producto"),
    path("detalle/<int:pk>/", ProductDetailView.as_view(), name="product_detail")
]
