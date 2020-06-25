import csv
import os

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = """Load products from CSV file. The CSV File must to be inside commands folder."""

    def get_full_path(self, csv_file):
        return os.path.join(os.path.dirname(__file__), csv_file)

    def handle(self, *args, **options):
        csv_file = self.get_full_path('products.csv')

        try:
            with open(csv_file, mode='r') as csv_file:
                csv_reader = csv.DictReader(
                    csv_file, delimiter=';',
                    quoting=csv.QUOTE_NONE,
                )

                for row in csv_reader:
                    # here create objects
                    pass
        except FileNotFoundError as error:
            raise CommandError(error)
