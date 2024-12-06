from django.urls import path, include
from .views import  ProductListView, ProductDetailView, buscar_producto, user_login, register, add_to_cart, view_cart



urlpatterns = [
    path("", ProductListView.as_view(), name="list_product"),
    path("detalle/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path('buscar/',  buscar_producto, name='buscar_producto')
]
