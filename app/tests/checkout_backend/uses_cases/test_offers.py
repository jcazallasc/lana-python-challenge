import csv
from unittest.mock import patch

from django.core.management import call_command
from django.test import TestCase

from checkout_backend.adapters.django.offer_repository import DjangoOfferRepository
from checkout_backend.adapters.django.product_repository import DjangoProductRepository
from checkout_backend.entities.offer_entity import OfferEntity
from checkout_backend.entities.product_entity import ProductEntity
from checkout_backend.management.commands.utils import get_full_path
from checkout_backend.models import Offer, Product
from checkout_backend.uses_cases.offers.factory_offer import FactoryOffer


class OffersTestCase(TestCase):

    def setUp(self):
        self.multi_buy_offer = OfferEntity(
            id=1,
            name='2x1',
            product=ProductEntity(
                id=1,
                code='TEST1',
                name='TEST1',
                price=500
            ),
            quantity=2,
            discount_unit=2,
            discount_percent=0,
        )

        self.depend_discount_offer = OfferEntity(
            id=1,
            name='3 or more discount 25%',
            product=ProductEntity(
                id=2,
                code='TEST2',
                name='TEST2',
                price=500
            ),
            quantity=3,
            discount_unit=0,
            discount_percent=25,
        )

    def test_apply_returns_true(self):
        """Test apply when product and quantity match"""

        offer_class = FactoryOffer().get_offer_class(self.multi_buy_offer)

        apply_result = offer_class.apply(
            self.multi_buy_offer.quantity,
            self.multi_buy_offer.product,
        )

        self.assertTrue(apply_result)

    def test_apply_returns_false_cause_product_wrong(self):
        """Test apply when quantity match but product doesn't match"""

        offer_class = FactoryOffer().get_offer_class(self.multi_buy_offer)

        apply_result = offer_class.apply(
            self.multi_buy_offer.quantity,
            self.depend_discount_offer.product,
        )

        self.assertFalse(apply_result)

    def test_apply_returns_false_cause_quantity_wrong(self):
        """Test apply when product match but quantity doesn't match"""

        offer_class = FactoryOffer().get_offer_class(self.multi_buy_offer)

        apply_result = offer_class.apply(
            self.multi_buy_offer.quantity - 1,
            self.multi_buy_offer.product,
        )

        self.assertFalse(apply_result)

    def test_get_subtotal_amount_depend_discount_offer(self):
        """Test get_subtotal_amount for multi buy offers"""

        offer_class = FactoryOffer().get_offer_class(self.multi_buy_offer)

        subtotal_amount = offer_class.get_subtotal_amount(
            self.multi_buy_offer.quantity,
            self.multi_buy_offer.product.price,
        )

        self.assertEqual(subtotal_amount, 500)

    def test_get_subtotal_amount_multi_buy_offer(self):
        """Test get_subtotal_amount for depend discount offers"""

        offer_class = FactoryOffer().get_offer_class(self.depend_discount_offer)

        subtotal_amount = offer_class.get_subtotal_amount(
            self.depend_discount_offer.quantity,
            self.depend_discount_offer.product.price,
        )

        self.assertEqual(subtotal_amount, 1125)
