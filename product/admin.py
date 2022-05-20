from django.contrib import admin
from .models import Product, Category, Color, Image, Manufacturer, Tag, FeaturedProduct, Review

# Register your models here.

class ImageInline(admin.StackedInline):
    model = Image
    can_delete = False
class ReviewInline(admin.StackedInline):
    model = Review
    can_delete = True

class ProductInline(admin.StackedInline):
    model = Product
    can_delete = False

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
        ImageInline,
    ]

# class ManufacturerAdmin(admin.ModelAdmin):
#     inlines = [
#         ProductInline,
#     ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Manufacturer #, ManufacturerAdmin
)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Color)
admin.site.register(Image)
admin.site.register(FeaturedProduct)
admin.site.register(Review)