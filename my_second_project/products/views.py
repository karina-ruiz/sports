from django.views import generic
from .models import Product, Cart, CartItem
from django.views.generic import DetailView
from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404


class ProductListView(generic.ListView):
    model = Product
    template_name = "product/add_product.html"
    context_object_name = "products"

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "product/detalles.html"
    context_object_name = "detalle"

    def get_queryset(self):
        pk = self.kwargs['pk'] 
        return Product.objects.filter(pk=pk)
    
def buscar_producto(request):
    products = []

    if 'buscar' in request.GET:
        search_term = request.GET['buscar']
        products = Product.objects.filter(article_name__icontains=search_term)
    return render(request, 'product/busquedas.html', {'products': products})

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [ 'username', 'email', 'password']

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'products/register.html', {'form': form})    

def user_login(request):
    if request.method == 'POST':
        username = request.POST['userme']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'cart.html', {'cart': cart})