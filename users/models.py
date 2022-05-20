from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from product.models import Product
from django.contrib.auth import get_user_model
from .manager import CustomUserManager

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=20)
    phone = models.CharField(max_length=11)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    






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