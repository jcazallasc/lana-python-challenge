from checkout_backend.interfaces.cart_repository import CartRepository
from checkout_backend.models import Cart, Product


class DjangoCartRepository(CartRepository):

    def create(self) -> Cart:
        return Cart.objects.create()

    def save(self, cart: Cart) -> Cart:
        cart.save()
        return cart

    def get(self, id: str) -> Cart:
        return Cart.objects.get(id=id)

    def add_product(self, cart: Cart, product: Product) -> Cart:
        cart.items[product.code] = 1
        cart.save()

        return cart

    def remove_product(self, cart: Cart, product: Product) -> Cart:
        cart.items[product.code] -= 1

        if not cart.items[product.code]:
            del cart.items[product.code]

        cart.save()

        return cart
