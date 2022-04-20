from pyexpat import model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model

from .models import Cart, Wishlist

CustomUser = get_user_model()
# Register your models here.

class UserCartInline(admin.StackedInline):
    model = Cart
    can_delete = True

class UserWishListInline(admin.StackedInline):
    model = Cart
    can_delete = True

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'email']
    inlines = (UserCartInline, UserWishListInline)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Cart)
admin.site.register(Wishlist)




# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User

# from my_user_profile_app.models import Employee

# # Define an inline admin descriptor for Employee model
# # which acts a bit like a singleton
# class EmployeeInline(admin.StackedInline):
#     model = Employee
#     can_delete = False
#     verbose_name_plural = 'employee'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (EmployeeInline,)

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)