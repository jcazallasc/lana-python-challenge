from checkout_backend.entities.cart_entity import CartEntity
from checkout_backend.entities.product_entity import ProductEntity
from checkout_backend.interfaces.cart_repository import CartRepository
from checkout_backend.models import Cart


class DjangoCartRepository(CartRepository):

    def create(self) -> CartEntity:
        return Cart.objects.create().to_entity()

    def get(self, id: str) -> CartEntity:
        return Cart.objects.get(id=id).to_entity()

    def get_items(self, cart: CartEntity) -> dict:
        return cart.items

    def add_item(self, cart: CartEntity, product: ProductEntity) -> CartEntity:
        cart_model = self._get(cart.id)

        if product.code in cart_model.items:
            cart_model.items[product.code] += 1
        else:
            cart_model.items[product.code] = 1

        cart_model.save()

        return cart_model.to_entity()

    def remove_item(self, cart: CartEntity, product: ProductEntity) -> CartEntity:
        cart_model = self._get(cart.id)

        cart_model.items[product.code] -= 1

        if not cart_model.items[product.code]:
            del cart_model.items[product.code]

        cart_model.save()

        return cart_model.to_entity()

    def _get(self, id: str) -> Cart:
        return Cart.objects.get(id=id)
