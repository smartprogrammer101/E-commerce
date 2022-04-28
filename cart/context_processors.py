from .cart import Cart
from product.models import Product


def cart(request):
    cart = Cart(request=request)
    # product_IDs = cart.get_product_IDs()
    # cart_items = Product.objects.filter(pk__in=product_IDs)
    copied_basket = cart.get_basket_with_product_itself_included()
    basket = copied_basket[0]
    subtotal = copied_basket[1]
    
    total_quantity = cart.get_total_quantity()

    # products_quantity_object = cart.get_products_quantity()
    # print(products_quantity_object)
    return {
        #'cart': cart_items, 
        'cart': basket,
        'subtotal': subtotal, 
    'total': total_quantity,# 'items_quantity': products_quantity_object}
    }