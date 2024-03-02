from rest_framework import serializers

from products.models import *


# class ProductListSerializer(serializers.ModelSerializer):
#     """
#     To show list of products.
#     """

#     class Meta:
#         model = Product
#         fields = ["name", "price"]


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "is_refrigerated", "ingredients"]


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SkuSerializer(serializers.ModelSerializer):
    markup_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Sku
        fields = "__all__"

    def get_markup_percentage(self, obj):
        return obj.markup_percentage
