from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem, Product
from django.http import HttpResponseRedirect
from django.contrib import messages



def cart(request):
    cart_id = request.session.get('cart_id')

    try:
        cart = Cart.objects.get(id=cart_id)
    except Cart.DoesNotExist:
        cart = None

    if cart is None:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    items = cart.items.all()
    context = {'cart': cart, 'items':items}
    return render(request, 'cart.html', context)

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_id = request.session.get('cart_id')
    print(f"cart_id: {cart_id}")

    try:
        cart = Cart.objects.get(id=cart_id)
    except Cart.DoesNotExist:
        cart = None

    if cart is None:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
        print(f"cart_id created: {cart.id}")

    quantity = int(request.POST.get('quantity', 1))
    # Kontrollera om varan redan finns i kundvagnen
    cart_items = cart.items.filter(product=product)
    if cart_items.exists():
        cart_item = cart_items.first()
        cart_item.update_quantity(cart_item.quantity + quantity)
        cart_item.save()
        cart.update_total()
        print(f"{product.name} quantity updated in your cart.")
    else:
        cart_item = CartItem.objects.create(cart=cart, product=product)
        cart.update_total()
        print(f"{product.name} has been added to your cart.")
    messages.success(request, f"{product.name} has been added to your cart.")
    return redirect('product_detail', product.id)
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.get(id=cart_id)

    try:
        cart_item = cart.items.get(product_id=product_id)
    except CartItem.DoesNotExist:
        # Produkten finns inte i kundvagnen
        messages.error(request, "This product is not in your cart.")
    else:
        # Produkten finns i kundvagnen, så ta bort den
        cart_item.delete()
        cart.update_total()
        messages.success(request, f"{product.name} has been removed from your cart.")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def update_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_id = request.session.get('cart_id')
    try:
        cart = Cart.objects.get(id=cart_id)
    except Cart.DoesNotExist:
        cart = None

    if cart is None:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    quantity = int(request.POST.get('quantity', 1))
    cart_items = cart.items.filter(product=product)

    if cart_items.exists():
        cart_item = cart_items.first()
        if quantity > 0:
            cart_item.update_quantity(quantity)
            cart_item.save()
            cart.update_total()
            messages.success(request, f"{product.name} quantity updated in your cart.")
        else:
            cart_item.delete()
            cart.update_total()
            messages.success(request, f"{product.name} removed from your cart.")
    else:
        if quantity > 0:
            CartItem.objects.create(cart=cart, product=product, quantity=quantity)
            messages.success(request, f"{product.name} added to your cart.")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def get_cart(request):
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(id=cart_id).first()
    return {'cart': cart}
