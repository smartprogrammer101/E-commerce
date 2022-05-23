from django.shortcuts import render
from django.views.generic import ListView
from product.models import Product, Category, Tag
from django.db.models import Q

# Create your views here.

# This view should only be viewed via a post request
class SearchedProductListView(ListView):
    model = Product
    template_name = 'search/search_result.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.GET.get('top_deal'):
            text = 'top deals'
            products = Product.objects.filter(discount__gt=0)
            context['searched_products_result'] = products
            context['searched_text'] = text
            context['searched_category'] = 'top deals'
            return context


        # If category is chosen during search
        if self.request.GET.get('category'):
            category = self.request.GET.get('category')
             # If category is chosen during search and text is inputed - filter products(text) in category
            if self.request.GET.get('q'):
                text = self.request.GET.get('q')
                products = Product.objects.filter(Q(name__icontains=text) & Q(category__name=category))
                context['searched_products_result'] = products
                context['searched_text'] = text
                context['searched_category'] = category
                return context
            
            # ELSE If category is chosen during search and text is NOT inputed - just filter by the category
            products = Product.objects.filter(category__name=category)
            context['searched_products_result'] = products
            context['searched_category'] = category
            return context
            
         
        # print(self.request.GET.get('category'))
        if self.request.GET.get('q'):
            searched_text = self.request.GET.get('q')
            context['searched_text'] = searched_text

            # If searched product in Category model
            in_category = Category.objects.filter(name__iexact=searched_text).exists()
            if in_category:
                products = Product.objects.filter(category__name__iexact=searched_text)
                context['searched_products_result'] = products
                return context

            # If searched product in Tag model
            in_tag = Tag.objects.filter(name__iexact=searched_text).exists()
            if in_tag:
                products = Product.objects.filter(tag__name__iexact=searched_text)
                context['searched_products_result'] = products
                return context
            
            # If searched product not in Category or Tag model - filter product directly in Product model
            products = Product.objects.filter(name__icontains=searched_text)
            context['searched_products_result'] = products
        return context
