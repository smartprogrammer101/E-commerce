from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=500)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    category = models.ManyToManyField('Category')
    tag = models.ManyToManyField('Tag')
    description = models.TextField(blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    in_stock = models.BooleanField(default=True)
    color = models.ManyToManyField('Color', default='unspecified')
    num_items = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
    
    


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    

class Color(models.Model):
    name = models.CharField(max_length=64, unique=True)
    
    def __str__(self):
        return self.name
    

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.image)
    