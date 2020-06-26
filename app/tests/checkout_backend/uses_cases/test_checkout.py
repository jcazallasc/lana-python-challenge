from django.core.management import call_command
from django.test import TestCase

from checkout_backend.adapters.django.cart_repository import DjangoCartRepository
from checkout_backend.adapters.django.offer_repository import DjangoOfferRepository
from checkout_backend.adapters.django.product_repository import DjangoProductRepository
from checkout_backend.entities.cart_entity import CartEntity
from checkout_backend.uses_cases.checkout import Checkout
from utils.formatters import format_price


class CheckoutTestCase(TestCase):

    def setUp(self):
        call_command('load_products')

        self.cart_repository = DjangoCartRepository()
        self.offer_repository = DjangoOfferRepository()
        self.product_repository = DjangoProductRepository()

        self.checkout = Checkout(
            cart_repository=self.cart_repository,
            product_repository=self.product_repository,
            offer_repository=self.offer_repository,
        )

        self.cart = self.cart_repository.create()

    def test_create_cart(self):
        """Test create cart using the user case"""

        cart_entity = self.checkout.create_cart()

        self.assertTrue(isinstance(cart_entity, CartEntity))

    def test_get_cart(self):
        """Test get cart using the uses case"""

        cart_entity = self.checkout.get_cart(self.cart.id)

        self.assertTrue(isinstance(cart_entity, CartEntity))
        self.assertEqual(cart_entity.id, self.cart.id)

    def test_add_product(self):
        """Test add product to cart"""

        product = self.product_repository.all()[0]

        cart_entity = self.checkout.add_product(self.cart.id, product.code)

        self.assertTrue(isinstance(cart_entity, CartEntity))
        self.assertEqual(len(cart_entity.items), 1)
        self.assertEqual(cart_entity.items[product.code], 1)

    def test_add_product_twice(self):
        """Test add product to cart twice"""

        product = self.product_repository.all()[0]

        self.checkout.add_product(self.cart.id, product.code)
        cart_entity = self.checkout.add_product(self.cart.id, product.code)

        self.assertTrue(isinstance(cart_entity, CartEntity))
        self.assertEqual(len(cart_entity.items), 1)
        self.assertEqual(cart_entity.items[product.code], 2)

    def test_remove_product(self):
        """Test remove product to cart"""

        product = self.product_repository.all()[0]

        # First, add 2 products
        self.checkout.add_product(self.cart.id, product.code)
        self.checkout.add_product(self.cart.id, product.code)

        cart_entity = self.checkout.remove_product(self.cart.id, product.code)

        self.assertTrue(isinstance(cart_entity, CartEntity))
        self.assertEqual(len(cart_entity.items), 1)
        self.assertEqual(cart_entity.items[product.code], 1)

    def test_remove_product_twice(self):
        """Test remove product to cart twice"""

        product = self.product_repository.all()[0]

        # First, add 2 products
        self.checkout.add_product(self.cart.id, product.code)
        self.checkout.add_product(self.cart.id, product.code)

        self.checkout.remove_product(self.cart.id, product.code)
        cart_entity = self.checkout.remove_product(self.cart.id, product.code)

        self.assertTrue(isinstance(cart_entity, CartEntity))
        self.assertEqual(len(cart_entity.items), 0)

    def test_get_total_amount(self):
        """Test get total amount"""

        product = self.product_repository.all()[0]

        # Add 2 products
        self.checkout.add_product(self.cart.id, product.code)
        cart_entity = self.checkout.add_product(self.cart.id, product.code)

        total_amount = self.checkout.get_total_amount(cart_entity)

        self.assertEqual(format_price(product.price * 2), total_amount)
