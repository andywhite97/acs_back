from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = "__all__"

class Sub_CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Sub_Category
        fields = "__all__"

class ConditionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Condition
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False)
    category = CategorySerializer(many=False)
    condition = ConditionSerializer(many=False)

    class Meta:
        model = Product
        fields = "__all__"

