from typing import List

from checkout_backend.interfaces.product_repository import ProductRepository
from checkout_backend.models import Product


class DjangoProductRepository(CartRepository):
    def get(self, code: str) -> Product:
        return Product.objects.get(code=code)

    def all(self) -> List[Product]:
        return Product.objects.all()
