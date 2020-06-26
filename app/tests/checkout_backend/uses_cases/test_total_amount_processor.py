from django.test import TestCase

from checkout_backend.entities.offer_entity import OfferEntity
from checkout_backend.entities.product_entity import ProductEntity
from checkout_backend.uses_cases.total_amount_processor import TotalAmountProcessor


class OffersTestCase(TestCase):

    def setUp(self):
        self.product_pen = ProductEntity(
            id=1,
            code='PEN',
            name='PEN',
            price=500,
        )
        self.product_tshirt = ProductEntity(
            id=2,
            code='TSHIRT',
            name='TSHIRT',
            price=2000,
        )
        self.product_mug = ProductEntity(
            id=3,
            code='MUG',
            name='MUG',
            price=750,
        )

        self.multi_buy_offer = OfferEntity(
            id=1,
            name='2x1',
            product=self.product_pen,
            quantity=2,
            discount_unit=1,
            discount_percent=0,
        )

        self.depend_discount_offer = OfferEntity(
            id=2,
            name='3 or more discount 25%',
            product=self.product_tshirt,
            quantity=3,
            discount_unit=0,
            discount_percent=25,
        )

        self.offers = [
            self.multi_buy_offer,
            self.depend_discount_offer,
        ]

        self.total_amount_processor = TotalAmountProcessor(self.offers)

    def test_get_total_amount_with_multi_buy_offer(self):
        """Test get total amount with a multi buy offer"""

        total_amount = self.total_amount_processor.get_total_amount(
            [
                {
                    'quantity': self.multi_buy_offer.quantity,
                    'product': self.multi_buy_offer.product,
                }
            ]
        )

        self.assertEqual(total_amount, 500)

    def test_get_total_amount_with_percent_discount_offer(self):
        """Test get total amount with percent discount amount"""

        total_amount = self.total_amount_processor.get_total_amount(
            [
                {
                    'quantity': self.depend_discount_offer.quantity,
                    'product': self.depend_discount_offer.product,
                }
            ]
        )

        self.assertEqual(total_amount, 4500)

    def test_get_total_amount_with_lane_case_1(self):
        """Test lana case 1"""

        total_amount = self.total_amount_processor.get_total_amount(
            [
                {
                    'quantity': 1,
                    'product': self.product_pen,
                },
                {
                    'quantity': 1,
                    'product': self.product_tshirt,
                },
                {
                    'quantity': 1,
                    'product': self.product_mug,
                },
            ],
        )

        self.assertEqual(total_amount, 3250)

    def test_get_total_amount_with_lane_case_2(self):
        """Test lana case 2"""

        total_amount = self.total_amount_processor.get_total_amount(
            [
                {
                    'quantity': 2,
                    'product': self.product_pen,
                },
                {
                    'quantity': 1,
                    'product': self.product_tshirt,
                },
            ],
        )

        self.assertEqual(total_amount, 2500)

    def test_get_total_amount_with_lane_case_3(self):
        """Test lana case 3"""

        total_amount = self.total_amount_processor.get_total_amount(
            [
                {
                    'quantity': 1,
                    'product': self.product_pen,
                },
                {
                    'quantity': 4,
                    'product': self.product_tshirt,
                },
            ],
        )

        self.assertEqual(total_amount, 6500)

    def test_get_total_amount_with_lane_case_4(self):
        """Test lana case 4"""

        total_amount = self.total_amount_processor.get_total_amount(
            [
                {
                    'quantity': 3,
                    'product': self.product_pen,
                },
                {
                    'quantity': 3,
                    'product': self.product_tshirt,
                },
                {
                    'quantity': 1,
                    'product': self.product_mug,
                },
            ],
        )

        self.assertEqual(total_amount, 6250)
