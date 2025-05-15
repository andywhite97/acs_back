
from django.urls import include, path
from .views import *

urlpatterns = [
    path('products/', GetProducts.as_view(), name='products'),
    path('brands/', GetBrands.as_view(), name='brands'),
    path('categories/', GetCategory.as_view(), name='categories'),
    path('sub_categories/', GetSubCategories.as_view(), name='sub_categories'),
    path('product/<int:pk>/', GetProduct.as_view(), name='product')
]
