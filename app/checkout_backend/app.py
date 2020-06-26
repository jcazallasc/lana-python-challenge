from .adapters.django.cart_repository import DjangoCartRepository
from .adapters.django.offer_repository import DjangoOfferRepository
from .adapters.django.product_repository import DjangoProductRepository
from .uses_cases.checkout import Checkout


class Application:
    def __init__(self):

        self.cart_repository = DjangoCartRepository()
        self.offer_repository = DjangoOfferRepository()
        self.product_repository = DjangoProductRepository()

        self.checkout = Checkout(
            cart_repository=self.cart_repository,
            product_repository=self.product_repository,
            offer_repository=self.offer_repository,
        )


app = Application()
