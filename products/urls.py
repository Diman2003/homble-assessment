from django.urls import path

from .views import *

urlpatterns = [
    path("", products_list, name="products-list"),
    path("create-sku/", CreateSkuView.as_view(), name="create-sku"),
    path(
        "product-detail/<int:pk>/", ProductDetailView.as_view(), name="product-detail"
    ),
    path(
        "update-sku-status/<int:pk>/",
        UpdateSkuStatusView.as_view(),
        name="update-sku-status",
    ),
    path(
        "active-categories-with-sku-count/",
        active_categories_with_sku_count,
        name="active_categories_with_sku_count",
    ),
    path(
        "all-skus-with-category/", all_skus_with_category, name="all_skus_with_category"
    ),
]
