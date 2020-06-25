import csv
import os

from django.core.management.base import BaseCommand, CommandError

from checkout_backend.models import Offer, Product


class Command(BaseCommand):
    help = """Load offers from CSV file. The CSV File must to be inside commands folder."""

    def get_full_path(self, csv_file):
        return os.path.join(os.path.dirname(__file__), csv_file)

    def handle(self, *args, **options):
        csv_file = self.get_full_path('offers.csv')

        try:
            with open(csv_file, mode='r') as csv_file:
                csv_reader = csv.DictReader(
                    csv_file, delimiter=';',
                    quoting=csv.QUOTE_NONE,
                )

                for row in csv_reader:
                    Offer.objects.update_or_create(
                        product=Product.objects.get(code=row['product_code']),
                        defaults={
                            'name': row['name'],
                            'quantity': int(row['quantity']),
                            'discount_unit': int(row['discount_unit']) if row['discount_unit'] else None,
                            'discount_percent': int(row['discount_percent']) if row['discount_percent'] else None,
                        },
                    )
        except FileNotFoundError as error:
            raise CommandError(error)
