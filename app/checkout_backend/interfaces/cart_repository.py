from checkout_backend.entities.cart_entity import CartEntity


class CartRepository:

    def create(self) -> CartEntity:
        raise NotImplementedError

    def get(self, id: str) -> CartEntity:
        raise NotImplementedError

    def get_items(self, cart: CartEntity) -> dict:
        raise NotImplementedError

    def add_item(self, cart: CartEntity, product: ProductEntity) -> CartEntity:
        raise NotImplementedError

    def remove_item(self, cart: CartEntity, product: ProductEntity) -> CartEntity:
        raise NotImplementedError
