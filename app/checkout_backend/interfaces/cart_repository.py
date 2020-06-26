from checkout_backend.entities.cart_entity import CartEntity
from checkout_backend.entities.product_entity import ProductEntity


class CartRepository:

    def create(self) -> CartEntity:
        raise NotImplementedError

    def delete(self, id: str) -> None:
        raise NotImplementedError

    def get(self, id: str) -> CartEntity:
        raise NotImplementedError

    def get_items(self, cart: CartEntity) -> dict:
        raise NotImplementedError

    def add_item(self, cart: CartEntity, product: ProductEntity) -> CartEntity:
        raise NotImplementedError

    def remove_item(self, cart: CartEntity, product: ProductEntity) -> CartEntity:
        raise NotImplementedError
