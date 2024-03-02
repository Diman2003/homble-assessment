# urls.py
from django.urls import path
from .views import CategoryWithProductsView

urlpatterns = [
    # ... other patterns
    path(
        "categories-with-products/",
        CategoryWithProductsView.as_view(),
        name="categories-with-products",
    ),
]
