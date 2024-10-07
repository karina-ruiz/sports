from django import forms 
from .models import Product

class ProductForm(forms.Form):
    article_name = forms.CharField(max_length=50, label="nombre_articulo")
    color = forms.CharField(max_length=50, label="color")
    price = forms.CharField(max_length=10, label="precio")
    size = forms.CharField(max_length=50, label="talla")
    photo = forms.ImageField(label="foto", required=False)

    def save(self):
        Product.objects.create(
            article_name=self.cleaned_data["name"],
            color=self.cleaned_data["color"],
            price=self.cleaned_data["price"],
            size=self.cleaned_data["size"],
            photo=self.cleaned_data["photo"],
        )