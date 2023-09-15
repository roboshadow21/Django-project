from django.core.management.base import BaseCommand
from myapp3.models import Product, Order, User


class Command(BaseCommand):
    help = "add orders to database"

    def handle(self, *args, **kwargs):
        user = User.objects.get(id=1)
        p1 = Product.objects.get(id=1)
        p2 = Product.objects.get(id=2)
        # p3 = Product.objects.get(id=3)
        # p4 = Product.objects.get(id=4)
        p5 = Product.objects.get(id=5)
        p6 = Product.objects.get(id=6)
        # order = Order(customer=user, total_price=(p1.price + p2.price), ordered_at="2023-9-7")
        # order2 = Order(customer=user, total_price=(p3.price + p4.price), ordered_at="2023-8-29")
        order3 = Order(customer=user, total_price=(p5.price + p6.price), ordered_at="2022-11-29")
        order3.save()
        order3.products.add(p5, p6)

        self.stdout.write(f'{order3}')
