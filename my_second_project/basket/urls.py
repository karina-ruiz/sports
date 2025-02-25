from django.urls import path
from . import views
app_name = 'basket' 

urlpatterns = [
    path('basket/', views.basket_summary, name='basket_summary'),
    path("add/", views.basket_add, name="basket_add"),
    path("delete/", views.basket_delete, name="basket_delete"),
    path("payment/", views.payment_form_view, name="basket_payment_form"),
    path('procesar_pago/', views.procesar_pago, name='procesar_pago'),
]
