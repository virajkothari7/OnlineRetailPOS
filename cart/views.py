# Create your views here.
from django.shortcuts import redirect
from inventory.models import product as Product
from django.contrib.auth.decorators import login_required
from .models import Cart


@login_required(login_url="/user/login")
def cart_add(request,id,qty):
    cart = Cart(request)
    product = Product.objects.filter(barcode=id).first()
    if product:
        cart.add(product=product,quantity=int(qty))
        return redirect('register')
    else:
        scheme = request.is_secure() and "https" or "http"
        return redirect(f"{scheme}://{request.get_host()}/register/ProductNotFound/")


@login_required(login_url="/user/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(barcode=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/user/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(barcode=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/user/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(barcode=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/user/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('register')

