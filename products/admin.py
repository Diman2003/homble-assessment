from django.contrib import admin
from products.models import Product, Sku

from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from products.models import Sku


# Update SkuAdmin to include markup_percentage
class SkuAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "size",
        "measurement_unit",
        "status",
        "markup_percentage",
    ]
    search_fields = ["product__name", "size"]
    autocomplete_fields = ["product"]


# Create Supervisors group
admin.site.unregister(Group)
supervisors_group, created = Group.objects.get_or_create(name="Supervisors")

# Add Sku edit permission to Supervisors
sku_permissions = Permission.objects.filter(
    content_type__app_label="products", codename__startswith="change_sku"
)
supervisors_group.permissions.set(sku_permissions)


class SkuInline(admin.TabularInline):
    model = Sku
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "is_refrigerated", "edited_at"]
    search_fields = ["name", "description", "ingredients"]
    ordering = ("-id",)
    list_filter = ("is_refrigerated", "category")
    fields = (
        "name",
        "category",
        "is_refrigerated",
        "description",
        "id",
        "created_at",
        "managed_by",
    )
    autocomplete_fields = ("category", "managed_by")
    readonly_fields = ("id", "created_at")
    exclude = ("edited_at",)
    inlines = [SkuInline]


class ProductInline(admin.StackedInline):
    """
    For display in CategoryAdmin
    """

    model = Product
    extra = 0
    ordering = ("-id",)
    fields = ("name", "is_refrigerated")  # Corrected line
    show_change_link = True


admin.site.register(Sku, SkuAdmin)

# management/commands/update_sku_prices.py
