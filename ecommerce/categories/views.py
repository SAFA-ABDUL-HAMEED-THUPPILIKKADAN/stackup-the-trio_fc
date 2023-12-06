from django.shortcuts import render
from .models import Category
from products.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    categories=Category.objects.all()
    context={'categories':categories}
    return render(request,'categories/index.html',context)

@login_required
def details(request,id):
    category=Category.objects.get(id=id)
    products=Product.objects.filter(category=category)
    context={'category':category,'products':products}
    return render(request,'categories/details.html',context)
