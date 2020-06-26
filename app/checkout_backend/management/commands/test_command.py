import csv

from django.core.management.base import BaseCommand, CommandError

from checkout_backend.adapters.django.offer_repository import DjangoOfferRepository
from checkout_backend.adapters.django.product_repository import DjangoProductRepository
from checkout_backend.management.commands.utils import get_full_path
from checkout_backend.uses_cases.total_amount_processor import TotalAmountProcessor


class Command(BaseCommand):
    help = """Load products from CSV file. The CSV File must to be inside commands folder."""

    def handle(self, *args, **options):
        product_repository = DjangoProductRepository()
        offer_repository = DjangoOfferRepository()

        offers = offer_repository.all()

        total_amount_processor = TotalAmountProcessor(offers)

        products = {
            'PEN': 3,
            'TSHIRT': 3,
            'MUG': 1,
        }

        data = {
            product_code: {
                'quantity': quantity,
                'product': product_repository.get(product_code)
            }
            for product_code, quantity in products.items()
        }

        total_amount = total_amount_processor.get_total_amount(data)

        print(total_amount)

        # PEN - 5.00
        # TSHIRT - 20.00
        # MUG - 7.50
