from django.core.management import BaseCommand

from user.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):

        user = CustomUser.objects.create(email='admin@example.com')
        user.set_password("1234567890")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()