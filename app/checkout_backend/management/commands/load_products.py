import csv

from django.core.management.base import BaseCommand, CommandError

from checkout_backend.adapters.django.django_product_repository import \
    DjangoProductRepository
from checkout_backend.management.commands.utils import get_full_path


class Command(BaseCommand):
    help = """Load products from CSV file. The CSV File must to be inside commands folder."""

    def handle(self, *args, **options):
        csv_file = get_full_path('products.csv')
        django_product_repository = DjangoProductRepository()

        try:
            with open(csv_file, mode='r') as csv_file:
                csv_reader = csv.DictReader(
                    csv_file, delimiter=';',
                    quoting=csv.QUOTE_NONE,
                )

                for row in csv_reader:
                    django_product_repository.update_or_create(
                        code=row['code'],
                        defaults={
                            'name': row['name'],
                            'price': float(row['price']) * 100,
                        },
                    )
        except FileNotFoundError as error:
            raise CommandError(error)
