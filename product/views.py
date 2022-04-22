from django.shortcuts import render
from django.views.generic import ListView
from .models import Product, Category, FeaturedProduct

# Create your views here.

class HomePageView(ListView):
    model = Product
    template_name = 'product/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()[:4]
        context["featured_products"] = FeaturedProduct.objects.all()[:4]
        return context

    def get_queryset(self):
        return Product.objects.all()[:4]
    
    