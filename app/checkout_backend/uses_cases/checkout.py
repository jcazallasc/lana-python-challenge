from utils.formatters import format_price

from ..entities.cart_entity import CartEntity
from ..interfaces.cart_repository import CartRepository
from ..interfaces.offer_repository import OfferRepository
from ..interfaces.product_repository import ProductRepository
from .total_amount_processor import TotalAmountProcessor


class Checkout:

    cart_repository = None
    product_repository = None
    offer_repository = None

    cart = None

    def __init__(
        self,
        cart_repository: CartRepository,
        product_repository: ProductRepository,
        offer_repository: OfferRepository,
    ):
        self.cart_repository = cart_repository
        self.product_repository = product_repository
        self.offer_repository = offer_repository

    def create_cart(self) -> CartEntity:
        return self.cart_repository.create()

    def delete_cart(self, id: str) -> CartEntity:
        return self.cart_repository.delete(id)

    def get_cart(self, id: str) -> CartEntity:
        return self.cart_repository.get(id)

    def add_product(self, cart: str, product_code: str) -> CartEntity:
        return self.cart_repository.add_item(
            self.get_cart(cart),
            self.product_repository.get(product_code),
        )

    def remove_product(self, cart: str, product_code: str) -> CartEntity:
        return self.cart_repository.remove_item(
            self.get_cart(cart),
            self.product_repository.get(product_code),
        )

    def get_items(self, cart: str) -> dict:
        return self._get_items(self.get_cart(cart))

    def _get_items(self, cart: CartEntity) -> dict:
        return [
            {
                'quantity': quantity,
                'product': self.product_repository.get(product_code)
            }
            for product_code, quantity in cart.items.items()
        ]

    def get_total_amount(self, cart: CartEntity) -> int:
        offers = self.offer_repository.all()

        total_amount_processor = TotalAmountProcessor(offers)

        data = self._get_items(cart)

        return format_price(total_amount_processor.get_total_amount(data))
