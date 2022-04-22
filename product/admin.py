from django.contrib import admin
from .models import Product, Category, Color, Image, Manufacturer, Tag, FeaturedProduct

# Register your models here.

class ImageInline(admin.StackedInline):
    model = Image
    can_delete = False

class ProductInline(admin.StackedInline):
    model = Product

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

class ManufacturerAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Color)
admin.site.register(Image)
admin.site.register(FeaturedProduct)
admin.site.register(Manufacturer, ManufacturerAdmin)