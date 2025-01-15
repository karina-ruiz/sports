from django.urls import path
from .views import  ProductListView, ProductDetailView, buscar_producto


urlpatterns = [
    path("", ProductListView.as_view(), name="list_product"),
    path("detalle/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path('buscar/', buscar_producto, name='buscar_producto')
]
