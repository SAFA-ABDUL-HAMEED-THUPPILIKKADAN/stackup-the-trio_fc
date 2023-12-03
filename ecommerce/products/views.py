from django.shortcuts import render,redirect
from .models import Product
from .forms import CreateProductForm,UpdateProductForm
from django.contrib.auth.decorators import login_required,user_passes_test

@login_required
def index(request):
    products=Product.objects.filter(user=request.user)
    context={'products':products}
    return render(request,'products/index.html',context)

@login_required
def details(request,id):
    product=Product.objects.get(id=id)
    context={'product':product}
    return render(request,'products/details.html',context)

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
@login_required
def create(request):
    if request.method=='POST':
        form=CreateProductForm(request.POST)
        if form.is_valid():
            created_product=form.save(commit=False)
            created_product.user=request.user
            created_product.save()
            return redirect('/products/')  

    form=CreateProductForm()    
    context={'form':form}
    return render(request,'products/create.html',context)

@login_required
def delete(request,id):
    product=Product.objects.get(id=id)
    product.delete()
    return redirect('/products/')  

@login_required
def update(request,id):
    product=Product.objects.get(id=id)

    if request.method=='POST':
        form=CreateProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect(f'/products/{product.id}')
    form=UpdateProductForm(instance=product)

    context={'product':product,'form':form}

    return render(request,'products/update.html',context)
    
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})




