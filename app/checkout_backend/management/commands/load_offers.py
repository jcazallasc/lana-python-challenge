import csv

from django.core.management.base import BaseCommand, CommandError

from checkout_backend.adapters.django.offer_repository import DjangoOfferRepository
from checkout_backend.adapters.django.product_repository import DjangoProductRepository
from checkout_backend.management.commands.utils import get_full_path


class Command(BaseCommand):
    help = """Load offers from CSV file. The CSV File must to be inside commands folder."""

    def handle(self, *args, **options):
        csv_file = get_full_path('offers.csv')
        offer_repository = DjangoOfferRepository()
        product_repository = DjangoProductRepository()

        try:
            with open(csv_file, mode='r') as csv_file:
                csv_reader = csv.DictReader(
                    csv_file, delimiter=';',
                    quoting=csv.QUOTE_NONE,
                )

                for row in csv_reader:
                    product_entity = product_repository.get(code=row['product_code'])
                    offer_repository.update_or_create(
                        product=product_entity,
                        defaults={
                            'name': row['name'],
                            'quantity': int(row['quantity']),
                            'discount_unit': int(row['discount_unit']) if row['discount_unit'] else None,
                            'discount_percent': int(row['discount_percent']) if row['discount_percent'] else None,
                        },
                    )
        except FileNotFoundError as error:
            raise CommandError(error)
