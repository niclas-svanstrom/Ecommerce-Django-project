from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse
from cart.models import Cart


def product_list(request):
    products = Product.objects.all()
    cart = get_or_create_cart(request)
    return render(request, 'product_list.html', {'products': products,'cart': cart})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    cart = get_or_create_cart(request)
    return render(request, 'product_detail.html', {'product': product, 'cart': cart})


def get_or_create_cart(request):
    # Försök hämta cart objektet från sessionen
    cart_id = request.session.get('cart_id')
    cart = None
    if cart_id:
        cart = get_object_or_404(Cart, id=cart_id)
    # Skapa nytt cart objekt om det inte finns något i sessionen
    if not cart:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    return cart