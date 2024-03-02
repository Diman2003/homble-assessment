# management/commands/update_sku_prices.py
from django.core.management.base import BaseCommand
from django.db.models import F
from products.models import Sku


class Command(BaseCommand):
    help = "Update SKU prices based on platform commission and cost price"

    def handle(self, *args, **options):
        # Update SKU prices
        Sku.objects.update(
            platform_commission=F("selling_price") * 0.25,
            cost_price=F("selling_price") - F("platform_commission"),
        )
        self.stdout.write(self.style.SUCCESS("SKU prices updated successfully"))
