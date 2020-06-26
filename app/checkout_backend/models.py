import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models

from checkout_backend.entities.cart_entity import CartEntity
from checkout_backend.entities.offer_entity import OfferEntity
from checkout_backend.entities.product_entity import ProductEntity


class EntityMixin:

    ENTITY = None

    def to_entity(self):
        data = {}
        for field in self._meta.fields:
            field_name = field.name
            field_value = getattr(self, field.name)

            if hasattr(field_value, 'to_entity'):
                field_value = field_value.to_entity()

            data[field_name] = field_value

        return self.ENTITY(
            **data
        )

class Product(models.Model, EntityMixin):

    ENTITY = ProductEntity

    code = models.CharField(
        max_length=20,
        unique=True,
    )

    name = models.CharField(
        max_length=250,
    )

    # For 7.50 => will store 750
    price = models.BigIntegerField()

    def __str__(self):
        return self.name


class Offer(models.Model, EntityMixin):

    ENTITY = OfferEntity

    name = models.CharField(
        max_length=60,
    )

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
    )

    # Quantity to know if discounts have to be applied
    quantity = models.IntegerField()

    # Discount per unit: buy 2 => get 1 free
    discount_unit = models.IntegerField(null=True, blank=True)

    # Discount per percent: buy > 3 => -25%
    discount_percent = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model, EntityMixin):

    ENTITY = CartEntity

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )

    items = JSONField(default=dict)

    def __str__(self):
        return str(self.id)
