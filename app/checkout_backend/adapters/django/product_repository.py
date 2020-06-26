from typing import List

from checkout_backend.entities.product_entity import ProductEntity
from checkout_backend.interfaces.product_repository import ProductRepository
from checkout_backend.models import Product


class DjangoProductRepository(ProductRepository):

    def update_or_create(self, code: str, defaults: dict) -> ProductEntity:
        product, created = Product.objects.update_or_create(
            code=code,
            defaults=defaults,
        )

        return product.to_entity()

    def get(self, code: str) -> ProductEntity:
        return Product.objects.get(code=code).to_entity()

    def all(self) -> List[ProductEntity]:
        return [product.to_entity() for product in Product.objects.all()]
