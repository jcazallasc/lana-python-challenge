from typing import List

from checkout_backend.entities.offer_entity import OfferEntity


class OfferRepository:

    def update_or_create(self, product_code: str, defaults: dict) -> OfferEntity:
        raise NotImplementedError

    def all(self) -> List[OfferEntity]:
        raise NotImplementedError
