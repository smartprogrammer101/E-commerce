from django.urls import path
from .views import SearchedProductListView

urlpatterns = [
    path('', SearchedProductListView.as_view(), name='search')
]
