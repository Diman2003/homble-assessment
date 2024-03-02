# categories/serializers.py
from rest_framework import serializers
from .models import *
from products.serializers import (
    ProductListSerializer,
)  # Assuming you have a products/serializers.py file


class CategorySerializer(serializers.ModelSerializer):
    count_products = serializers.ReadOnlyField()
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
