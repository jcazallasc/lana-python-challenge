from .base_offer import BaseOffer


class MultiBuyOffer(BaseOffer):

    def get_subtotal_amount(
        self,
        product_quantity: int,
        product_price: int,
    ) -> int:

        num_free_products = product_quantity // self.offer.quantity

        return (product_quantity - num_free_products) * product_price
