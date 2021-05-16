from django.core.management.base import BaseCommand
from ...models import Product


class Command(BaseCommand):
    help = "sandbox command"
    model = Product

    def handle(self, *args, **options):
        duplicate_product = self.model.ready_for_sale.first()
        duplicate_product.pk = None
        duplicate_products = []
        for i in range(20):
            duplicate_products.append(duplicate_product)
        self.model.objects.bulk_create(duplicate_products)
