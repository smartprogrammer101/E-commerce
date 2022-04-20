from django.db import models
from django.contrib.auth.models import AbstractUser
from product.models import Product
from django.contrib.auth import get_user_model

# Create your models here.

class CustomUser(AbstractUser):
    pass

class Cart(models.Model):
    product = models.ManyToManyField(Product)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
    

class Wishlist(models.Model):
    product = models.ManyToManyField(Product)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)