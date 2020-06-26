from ..adapters.django.cart_repository import CartRepository
from ..adapters.django.offer_repository import OfferRepository
from ..adapters.django.product_repository import ProductRepository
from ..entities.cart_entity import CartEntity
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

    def get_cart(self, id: str) -> CartEntity:
        return self.cart_repository.get(id)

    def add_product(self, cart: CartEntity, product_code: str) -> CartEntity:
        return self.cart_repository.add_item(
            cart,
            self.product_repository.get(product_code),
        )

    def remove_product(self, cart: CartEntity, product_code: str) -> CartEntity:
        return self.cart_repository.remove_item(
            cart,
            self.product_repository.get(product_code),
        )

    def get_total_amount(self, cart: CartEntity) -> int:
        products = self.cart_repository.get_items(cart)
        offers = self.offer_repository.all()

        total_amount_processor = TotalAmountProcessor(offers)

        data = {
            product_code: {
                'quantity': quantity,
                'product': self.product_repository.get(product_code),
            }
            for product_code, quantity in products.items()
        }

        return total_amount_processor.get_total_amount(data)
