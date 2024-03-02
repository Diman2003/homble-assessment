from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework import status

from django.http import JsonResponse
from django.db.models import Count, Q

from categories.models import Category

from .models import Product
from .serializers import ProductListSerializer

from rest_framework import generics, permissions
from products.models import *
from products.serializers import *


@api_view(["GET"])
@permission_classes([AllowAny])
def products_list(request):
    """
    List of all products, with optional filtering based on the 'refrigerated' query parameter.
    """
    try:
        refrigerated_param = request.query_params.get("refrigerated", None)

        if refrigerated_param is not None:
            # Filter products based on the refrigerated parameter
            products = Product.objects.filter(
                is_refrigerated=(refrigerated_param.lower() == "true")
            )
        else:
            # Show all products by default
            products = Product.objects.all()

        serializer = ProductListSerializer(products, many=True)
        return Response({"products": serializer.data}, status=HTTP_200_OK)
    except Exception as e:
        return Response({"error":f"{e}"} , status=status.HTTP_400_BAD_)


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CreateSkuView(generics.CreateAPIView):
    queryset = Sku.objects.all()
    serializer_class = SkuSerializer
    permission_classes = [AllowAny]  # Adjust based on your requirements


class UpdateSkuStatusView(generics.UpdateAPIView):
    queryset = Sku.objects.all()
    serializer_class = SkuSerializer
    permission_classes = [permissions.IsAdminUser]


def active_categories_with_sku_count(request):
    try:
        active_categories = Category.objects.filter(
            products__sku__status=1,  # Assuming 'Approved' status has the value of 1
            is_active=True,
        ).distinct().annotate(
            approved_sku_count=Count('products__sku', filter=Q(products__sku__status=1))
        )

        # Output the data as JSON for simplicity, adapt as needed
        data = [{'category_name': category.name, 'approved_sku_count': category.approved_sku_count} for category in active_categories]

        return JsonResponse({'active_categories_with_sku_count': data})
    except Exception as e:
        return Response({"error":f"{e}"} , status=status.HTTP_400_BAD_)





def all_skus_with_category(request):
    try:
        all_skus = Sku.objects.select_related("product__category").all()

        # Output the data as JSON for simplicity, adapt as needed
        data = [
            {
                "sku_id": sku.id,
                "sku_size": sku.size,
                "category_name": sku.product.category.name if sku.product.category else None,
            }
            for sku in all_skus
        ]

        return JsonResponse({"all_skus_with_category": data})
    except Exception as e:
        return Response({"error":f"{e}"} , status=status.HTTP_400_BAD_)
