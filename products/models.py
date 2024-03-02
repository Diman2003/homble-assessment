from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.core.validators import MaxValueValidator


class Product(models.Model):
    """
    Very basic structure. To be further built up.
    """

    name = models.CharField(
        _("display name"),
        max_length=150,
        unique=True,
        help_text=_("This will be displayed to the user as-is"),
    )
    # price = models.PositiveSmallIntegerField(
    #     _("selling price (Rs.)"),
    #     help_text=_("Price payable by the customer (Rs.)"),
    # )
    description = models.TextField(
        _("descriptive write-up"),
        unique=True,
        help_text=_("Few sentences that showcase the appeal of the product"),
    )
    is_refrigerated = models.BooleanField(
        help_text=_("Whether the product needs to be refrigerated"),
        default=False,
    )
    ingredients = models.CharField(
        _("ingredients"),
        max_length=500,
        help_text=_("List of ingredients, maximum 500 characters"),
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        "categories.Category",
        related_name="products",  # Corrected related_name
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )
    managed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="managed_products",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True, editable=True)

    def save(self, *args, **kwargs):
        self.name = self.name.strip().title()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "product"
        ordering = []
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Sku(models.Model):
    UNIT_CHOICES = [
        ("gm", "Gram"),
        ("kg", "Kilogram"),
        ("mL", "Milliliter"),
        ("L", "Liter"),
        ("pc", "Piece"),
    ]

    STATUS_CHOICES = [
        (0, "Pending for Approval"),
        (1, "Approved"),
        (2, "Discontinued"),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(999)], null=True, blank=True
    )
    measurement_unit = models.CharField(
        max_length=3, choices=UNIT_CHOICES, null=True, blank=True
    )
    selling_price = models.PositiveSmallIntegerField(null=True, blank=True)
    platform_commission = models.PositiveSmallIntegerField(null=True, blank=True)
    cost_price = models.PositiveSmallIntegerField(null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0)

    def save(self, *args, **kwargs):
        # Override the save method to set default status
        if not self.status:
            self.status = 0
        super().save(*args, **kwargs)

    @property
    def markup_percentage(self):
        if self.cost_price == 0:
            return None
        return (self.platform_commission / self.cost_price) * 100

    def __str__(self):
        return f"{self.product.name} - {self.size} gm (Rs. {self.cost_price})"
