from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        # user = User(name='John', email='john@example.com', phone='123-456-789',
        #             address='Moscow, Some Street, 48')
        user = User(name='Bob', email='bob@example.com', phone='321-654-987',
                    address='Moscow, Some Street, 48')

        user.save()
        self.stdout.write(f'{user}')
