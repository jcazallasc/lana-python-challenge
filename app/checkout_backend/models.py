import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models


class Product(models.Model):

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


class Offer(models.Model):

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


class Cart(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )

    items = JSONField()

    def __str__(self):
        return self.id
