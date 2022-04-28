from django.shortcuts import render, redirect
from .cart import Cart

# Create your views here.

def cart(request):
    product_id = request.POST.get('product-id')
    quantity = request.POST.get('quantity')
    print(request.POST.get('type'))
    
    item = Cart(request, product_id, quantity)
    if request.method == 'POST':
        if request.POST.get('type') == 'DELETE':
            item.remove_from_cart(request, product_id)
        else:
            item.add_to_cart()
    return render(request, 'cart/cart.html')

# def add_to_cart(request):
#     return redirect('home')