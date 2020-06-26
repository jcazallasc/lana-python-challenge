from .base_offer import BaseOffer


class DependDiscountOffer(BaseOffer):

    def get_subtotal_amount(
        self,
        product_quantity: int,
        product_price: int,
    ) -> int:
        return product_quantity * product_price * (100 - self.offer.discount_percent) / 100
