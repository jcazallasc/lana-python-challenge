from typing import Union

from checkout_backend.entities.offer_entity import OfferEntity

from .depend_discount_offer import DependDiscountOffer
from .multi_buy_offer import MultiBuyOffer


class FactoryOffer:

    OFFER_MAP = {
        'discount_unit': MultiBuyOffer,
        'discount_percent': DependDiscountOffer,
    }

    def get_offer_class(self, offer: OfferEntity) -> Union[MultiBuyOffer, DependDiscountOffer]:
        if offer.discount_unit:
            return self.OFFER_MAP['discount_unit'](offer)
        elif offer.discount_percent:
            return self.OFFER_MAP['discount_percent'](offer)
