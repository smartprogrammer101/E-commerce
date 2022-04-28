from itertools import product
from django.test import TestCase
from django.urls import reverse
from .cart import Cart
from product.models import Product, Category, Color, FeaturedProduct, Image, Manufacturer, Tag

# Create your tests here.

class TestCartFunctionality(TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer.objects.create(name='Coca Cola')
        self.category = Category.objects.create(name='Drink')
        self.tag1 = Tag.objects.create(name='drink')
        self.tag2 = Tag.objects.create(name='pepsi')
        self.color = Color.objects.create(name='red')
        self.product = Product.objects.create(
            name = 'Pepsi',
            manufacturer = self.manufacturer,
            price = 2499.99,
            discount = 0,
            rating = 0,
            num_items = 1000,
            in_stock = True,
        )
        self.product.category.set([self.category])
        self.product.tag.set([self.tag1, self.tag2])
        self.product.color.set([self.color])

        self.image = Image.objects.create(image='image.png', product=self.product)
        self.featured_product = FeaturedProduct.objects.create(product=self.product)

        url = reverse('cart:cart')
        self.request = self.client.post(url, {'product-id': self.product.id, 'quantity': 4})
        self.cart = Cart(self.client, product_id=self.product.id)

    def test_cart_template(self):
        url = reverse('cart:cart')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')
        
    def test_item_added_to_cart(self):
        self.cart.add_to_cart()
        self.assertTrue(self.client.session.has_key('cart'))
        self.assertTrue(str(self.product.id) in self.client.session['cart'])

    def test_item_remove_from_cart(self):
        self.assertTrue(str(self.product.id) in self.client.session['cart'])
        self.cart.remove_from_cart(self.client, str(self.product.id))
        # self.assertFalse(str(self.product.id) in self.client.session['cart'])

# class TestCartFunctionality(TestCase):
#     def setUp(self):
#         self.manufacturer = Manufacturer.objects.create(name='Coca Cola')
#         self.category = Category.objects.create(name='Drink')
#         self.tag1 = Tag.objects.create(name='drink')
#         self.tag2 = Tag.objects.create(name='pepsi')
#         self.color = Color.objects.create(name='red')
#         self.product = Product.objects.create(
#             name = 'Pepsi',
#             manufacturer = self.manufacturer,
#             price = 2499.99,
#             discount = 0,
#             rating = 0,
#             num_items = 1000,
#             in_stock = True,
#         )
#         self.product.category.set([self.category])
#         self.product.tag.set([self.tag1, self.tag2])
#         self.product.color.set([self.color])

#         self.image = Image.objects.create(image='image.png', product=self.product)
#         self.featured_product = FeaturedProduct.objects.create(product=self.product)

#         self.url = reverse('cart:cart')
#         self.request = self.client.post(self.url, {'product-id': self.product.id, 'quantity': 4})
#         self.request = self.request.client
#         self.cart = Cart(self.request, product_id=self.product.id)

#     def test_cart_template(self):
#         url = reverse('cart:cart')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'cart/cart.html')
        
#     def test_item_added_to_cart(self):
#         self.cart.add_to_cart()
#         self.assertTrue(self.request.session.has_key('cart'))
#         self.assertTrue(str(self.product.id) in self.request.session['cart'])
#         # self.cart.remove_from_cart(self.request, str(self.product.id))
#         # self.assertFalse(str(self.product.id) in request.session['cart'])

#     def test_item_remove_from_cart(self):
#         # request = self.client.post(self.url, {'product-id': self.product.id, 'type': 'DELETE'})
#         # request = request.client
#         self.assertTrue(str(self.product.id) in self.request.session['cart'])
#         self.cart.remove_from_cart(self.request, str(self.product.id))
#         self.assertFalse(str(self.product.id) in self.request.session['cart'])