from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from products.models import Product
from .basket import Basket
from .form import PaymentForm


def basket_summary(request):
    return render(request, "basket/summary.html")



def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)


        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)
        response = JsonResponse({'Success': True})
        return response


def payment_form_view(request):
    form = PaymentForm()
    return render(request, 'basket/form_cart.html', {'form': form})

def procesar_pago(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            print("Formulario válido")
            print(form.cleaned_data)
            form.save()
            basket = Basket(request)
            purchased_products = list(basket)
            basket.clear()
            return render(request, 'basket/pago_exitoso.html', {'nombre': form.cleaned_data['name_cart'], 'monto': form.cleaned_data['cvv'], 'productos': purchased_products})
        else:
            print("Formulario no válido")
            print(form.errors)
    else:
        form = PaymentForm()
    return render(request, 'basket/form_cart.html', {'form': form})