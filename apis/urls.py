
from django.urls import include, path
from .views import *

urlpatterns = [
    path('products/', GetProducts.as_view(), name='home'),
    path('brands/', GetBrands.as_view(), name='home'),
    path('categories/', GetCategory.as_view(), name='home'),
    path('sub_categories', GetSubCategories.as_view(), name='home'),
    path('product/<int:pk>/', GetProduct.as_view(), name='home')
]
