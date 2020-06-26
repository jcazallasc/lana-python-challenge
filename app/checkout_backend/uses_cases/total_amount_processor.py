from typing import List

from checkout_backend.entities.offer_entity import OfferEntity

from .offers.factory_offer import FactoryOffer


class TotalAmountProcessor:

    offers = None
    product = None
    quantity = None

    def __init__(self, offers: List[OfferEntity]):
        self.offers = offers

    def get_total_amount(self, products: dict) -> int:
        """
        Calculate the total amount of a list of products.

        product: Dict in which the keys are product_codes. Inside each item, there are quantity (int)
                 and product (ProductEntity) keys.

        {
            'PEN': {
                'quantity': 1,
                'product': ProductEntity(...)
            },
            ...
        }
        """

        total_amount = 0
        factory_offer = FactoryOffer()

        for product_code, product_data in products.items():
            quantity = product_data['quantity']
            product = product_data['product']

            subtotal_amount = product.price * quantity

            for offer in self.offers:
                offer_class = factory_offer.get_offer_class(offer)

                if offer_class.apply(quantity, product):
                    subtotal_amount = offer_class.get_subtotal_amount(quantity, product.price)

                    # Just allow one offer match
                    break

            total_amount += subtotal_amount

        return total_amount
