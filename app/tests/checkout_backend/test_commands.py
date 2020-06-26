import csv

from django.core.management import call_command
from django.test import TestCase

from checkout_backend.management.commands.utils import get_full_path
from checkout_backend.models import Offer, Product


class CommandsTestCase(TestCase):

    def _get_num_lines_from_csv(self, filename):
        """Return the number of lines in the CSV file inside commands folder"""

        _file = open(get_full_path(filename))
        _reader = csv.reader(_file)

        return len(list(_reader))

    def test_load_products(self):
        """Test load products from CSV file"""

        call_command('load_products')

        products_count = Product.objects.all().count()

        self.assertEqual(
            products_count + 1,
            self._get_num_lines_from_csv('products.csv'),
        )

    def test_load_products_twice(self):
        """Test load products from CSV file twice to check no errors raise"""

        call_command('load_products')
        call_command('load_products')

        products_count = Product.objects.all().count()

        self.assertEqual(
            products_count + 1,
            self._get_num_lines_from_csv('products.csv'),
        )

    def test_load_offers_from_csv(self):
        """Test load offers from CSV file"""

        # Offer needs products
        call_command('load_products')

        call_command('load_offers')

        offers_rates = Offer.objects.all().count()

        self.assertEqual(
            offers_rates + 1,
            self._get_num_lines_from_csv('offers.csv'),
        )

    def test_load_offers_from_csv_twice(self):
        """Test load offers from CSV file twice to check no errors raise"""

        # Offer needs products
        call_command('load_products')

        call_command('load_offers')
        call_command('load_offers')

        offers_rates = Offer.objects.all().count()

        self.assertEqual(
            offers_rates + 1,
            self._get_num_lines_from_csv('offers.csv'),
        )
