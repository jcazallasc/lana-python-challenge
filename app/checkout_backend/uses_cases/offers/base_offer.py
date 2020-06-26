from checkout_backend.entities.product_entity import ProductEntity


class BaseOffer:

    offer = None

    def __init__(self, offer):
        self.offer = offer

    def apply(
        self,
        product_quantity: int,
        product: ProductEntity,
    ) -> bool:
        return self.offer.product.id == product.id and product_quantity >= self.offer.quantity

    def get_subtotal_amount(
        self,
        product_quantity: int,
        product_price: int,
    ) -> int:
        raise NotImplementedError
