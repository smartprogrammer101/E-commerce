from django.test import TestCase
from .models import Category, Product, Tag, Manufacturer, Image, Color

# Create your tests here.

class TestDatabaseCorrectness(TestCase):
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

    def test_new_product_entry(self):
        self.assertEqual(self.product.name, 'Pepsi')
        self.assertEqual(self.product.manufacturer.name, 'Coca Cola')
        self.assertEqual(self.product.category.first().name, 'Drink')
        self.assertEqual(self.product.color.first().name, 'red')
        self.assertEqual(self.product.tag.first().name, 'drink')
        self.assertEqual(self.product.tag.last().name, 'pepsi')
        self.assertEqual(self.product.price, 2499.99)
        self.assertEqual(self.product.discount, 0)
        self.assertEqual(self.product.rating, 0)
        self.assertEqual(self.product.num_items, 1000)
        self.assertEqual(self.product.in_stock, True)
        self.assertEqual(self.product.image_set.first().image, 'image.png')

    def test_image_entry(self):
        '''>>>> Check when image is stored in the database <<<<'''
        self.assertEqual(self.product.image_set.first().image, 'image.png')
        self.assertEqual(self.product.image_set.first().image.url, '/media/image.png')

    def test_str_format(self):
        '''>>>> Check the string format of all database entries <<<<'''
        self.assertEqual(str(self.product), 'Pepsi')
        self.assertEqual(str(self.manufacturer), 'Coca Cola')
        self.assertEqual(str(self.category), 'Drink')
        self.assertEqual(str(self.color), 'red')
        self.assertEqual(str(self.tag1), 'drink')
        self.assertEqual(str(self.tag2), 'pepsi')
        self.assertEqual(str(self.image), 'image.png')


# from product.models import Category, Color, Image, Manufacturer, Product, Tag
# manufacturer = Manufacturer.objects.create(name='Coca Cola')
# product = Product.objects.create(name = 'Pepsi',manufacturer = manufacturer,price = 2499.99,discount = 0,rating = 0,num_items = 1000,in_stock = True,)
# color = Color.objects.create(name='red')

# color.product = product