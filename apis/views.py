from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

#Get an array of all products
class GetProducts(APIView):
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
#Get an array of all brands
class GetBrands(APIView):
    
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
#Get an array of all category
class GetCategory(APIView):
    
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
#Get an array of all sub_category
class GetSubCategories(APIView):
    
    def get(self, request):
        categories = Sub_Category.objects.all()
        serializer = Sub_CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
#Get a product
class GetProduct(APIView):
    
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK) 
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        