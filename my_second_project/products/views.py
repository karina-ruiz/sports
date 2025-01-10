from django.views import generic
from .models import Product
from django.shortcuts import render
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
class ProductListView(generic.ListView):
    model = Product
    template_name = "Product/add_product.html"
    context_object_name = "products"

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "Product/detalles.html"
    context_object_name = "detalle"

    def get_queryset(self):
        pk = self.kwargs['pk'] 
        return Product.objects.filter(pk=pk)
    
def buscar_producto(request):
    products = []

    if 'buscar' in request.GET:
        search_term = request.GET['buscar']
        products = Product.objects.filter(article_name__icontains=search_term)
    return render(request, 'Product/busquedas.html', {'products': products})
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