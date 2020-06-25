from typing import List

from checkout_backend.entities.product_entity import ProductEntity


class ProductRepository:

    def update_or_create(self, code: str, defaults: dict) -> ProductEntity:
        raise NotImplementedError

    def get(self, code: str) -> ProductEntity:
        raise NotImplementedError

    def all(self) -> List[ProductEntity]:
        raise NotImplementedError
