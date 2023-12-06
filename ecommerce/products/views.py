from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Cart
from .forms import CreateProductForm,UpdateProductForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib import messages


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
        form=CreateProductForm(request.POST,request.FILES)
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
    

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
    

@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product,id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Add the product to the user's cart
    cart.products.add(product)
    products=cart.products.all()
    total_price = sum(item.price for item in products)
    messages.success(request, f"{product.name} added to your cart.")
    return render(request,'products/cart.html',{'products':products,'total_price':total_price})


@login_required
def remove_from_cart(request, id):
    product = get_object_or_404(Product,id=id)
    cart = get_object_or_404(Cart, user=request.user)
    
    # Remove the product from the user's cart
    cart.products.remove(product)
    total_price = sum(item.price for item in cart.products.all())
    products=cart.products.all()

    messages.success(request, f"{product.name} removed from your cart.")
    
    # Redirect the user back to the cart
    return render(request,'products/cart.html',{'products':products,'cart': cart, 'total_price': total_price})

