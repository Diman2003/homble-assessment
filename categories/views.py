# views.py
from rest_framework.views import APIView
from rest_framework.response import Response

# from rest_framework.permissions import IsAdminUser
from .models import Category
from .serializers import CategorySerializer
from rest_framework.permissions import AllowAny


class CategoryWithProductsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
