# from decimal import Decimal
from urllib import request
from product.models import Product

class Cart():
    def __init__(self, request, product_id=None, quantity=None):
        self.product_id = product_id
        self.quantity = quantity

        basket = request.session.get('cart')
        if 'cart' not in request.session:
            request.session['cart'] = {}
            basket = request.session.get('cart')
        self.basket = basket
        request.session.modified = True

        self.session = request.session

    def add_to_cart(self):
        # if self.product_id in self.basket:
        product = Product.objects.get(pk=self.product_id)
        self.basket[self.product_id] = {'qty': self.quantity,# 'product': product}
        }
        self.session.modified = True

    def remove_from_cart(self, request, id):
        # del self.basket[id]
        # print(request.session['cart'])
        basket = request.session['cart']
        del basket[id]
        request.session.modified = True

    def get_basket_with_product_itself_included(self):
        IDs = []
        cart_list = []
        subtotal = 0
        products_IDs = self.basket.keys()
        for id in products_IDs:
            IDs.append(id)
        products = Product.objects.filter(pk__in=products_IDs)
        for product in products:
            cart_dict = {}
            cart_dict['product'] = product
            cart_dict['quantity'] = self.basket[str(product.id)]['qty']
            # cart_dict['total'] = Decimal.from_float(float(cart_dict['quantity'])) * product.price
            cart_dict['total'] = int(cart_dict['quantity']) * product.price
            subtotal += cart_dict['total']
            cart_list.append(cart_dict)
        return [cart_list, subtotal]

    def get_total_quantity(self):
        IDs = []
        products_qty = self.basket.values()
        for product in products_qty:
            IDs.append(int(product['qty']))
        return sum(IDs)

    def get_products_quantity(self):
        obj = {}
        for k,v in self.basket.items():
            product_id = k
            quantity = int(v['qty'])
            obj[product_id] = quantity
        return obj