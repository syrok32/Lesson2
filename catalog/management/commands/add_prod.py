from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Add test books to the database'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        сategory, _ = Category.objects.get_or_create(name='телефон', description='современный гаджеты')

        phone = [
            {'name': 'POCO X3', 'description': 'грееться', 'category': сategory, 'price': 20000},
            {'name': 'iPone 10', 'description': 'fast', 'category': сategory, 'price': 230000},
        ]

        for book_data in phone:
            phone, created = Product.objects.get_or_create(**book_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added book: {phone.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Book already exists: {phone.name}'))