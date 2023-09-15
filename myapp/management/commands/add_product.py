from django.core.management.base import BaseCommand
from myapp3.models import Product


class Command(BaseCommand):
    help = "Add new product"

    def handle(self, *args, **kwargs):
        product = Product(name="product6", description="Product 6", price=31, quantity=7,
                          added_at="2022-12-15")
        product.save()
        self.stdout.write(f'{product}')
