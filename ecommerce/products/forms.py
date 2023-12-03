from django.forms import ModelForm
from .models import Product

class CreateProductForm(ModelForm):
    class Meta:
        model=Product
        fields=('name','price','stock','category')


class UpdateProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'        