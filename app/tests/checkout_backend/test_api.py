import json
from datetime import date
from unittest.mock import MagicMock, patch

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from checkout_backend.adapters.django.cart_repository import DjangoCartRepository

CREATE_CART = 'create-cart'
DELETE_CART = 'delete-cart'
CART_ADD_PRODUCT = 'cart-add-product'
CART_REMOVE_PRODUCT = 'cart-remove-product'


class ExoCurrencyV1ApiTests(TestCase):
    """Test for the API V1 of exo_currency"""

    def setUp(self):
        self.client = APIClient()

        call_command('load_products')
        call_command('load_offers')

        self.cart_repository = DjangoCartRepository()

    def test_create_cart(self):
        """Test creating cart"""

        res = self.client.post(reverse(CREATE_CART))

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(res.data['cart']['items']), 0)
        self.assertEqual(int(res.data['total_amount']), 0)

    def test_delete_existing_cart(self):
        """Test delete existing cart"""

        res = self.client.post(reverse(CREATE_CART))

        url = reverse(
            DELETE_CART,
            kwargs={
                'cart_id': res.data['cart']['id'],
            },
        )

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_cart_non_existing_cart(self):
        """Test delete non existing cart"""

        url = reverse(
            DELETE_CART,
            kwargs={
                'cart_id': 'd59cc187-d2ac-4bb7-a2f9-3b96909f80ca',
            },
        )

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_cart_with_malformed_uuid(self):
        """Test delete cart with malformed uuid"""

        url = reverse(
            DELETE_CART,
            kwargs={
                'cart_id': 'asdf',
            },
        )

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_cart_add_product(self):
        """Test cart add product"""

        res = self.client.post(reverse(CREATE_CART))

        url = reverse(
            CART_ADD_PRODUCT,
            kwargs={
                'cart_id': res.data['cart']['id'],
                'product_code': 'PEN',
            },
        )

        res = self.client.post(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_cart_add_product_with_wrong_data(self):
        """Test cart add product with wrong data"""

        res = self.client.post(reverse(CREATE_CART))

        url = reverse(
            CART_ADD_PRODUCT,
            kwargs={
                'cart_id': res.data['cart']['id'],
                'product_code': 'asdasdasd',
            },
        )

        res = self.client.post(url)

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_cart_remove_product(self):
        """Test cart remove product"""

        res = self.client.post(reverse(CREATE_CART))

        url = reverse(
            CART_REMOVE_PRODUCT,
            kwargs={
                'cart_id': res.data['cart']['id'],
                'product_code': 'PEN',
            },
        )

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_cart_remove_product_with_wrong_data(self):
        """Test cart remove product with wrong data"""

        res = self.client.post(reverse(CREATE_CART))

        url = reverse(
            CART_REMOVE_PRODUCT,
            kwargs={
                'cart_id': res.data['cart']['id'],
                'product_code': 'asdasdasd',
            },
        )

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
