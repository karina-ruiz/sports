from django.views import generic
from .models import Product, Categoria
from django.shortcuts import render, get_object_or_404
class ProductListView(generic.ListView):
    model = Product
    template_name = "base.html"
    context_object_name = "products"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        categoria_id = kwargs.get('categoria_id')
        if categoria_id:
            context['productos_categoria'] = Product.objects.filter(categoria__id=categoria_id)
        return context


def categoria_detalle(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    products = Product.objects.filter(categoria=categoria)
    print(f'Número de productos en la categoría {categoria.nombre}: {len(products)}')
    return render(request, 'product/lista_categorias.html', {
        'categoria': categoria,
        'products': products,
    })

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
        products = Product.objects.filter(name__icontains=search_term)
    return render(request, 'Product/busquedas.html', {'products': products})

