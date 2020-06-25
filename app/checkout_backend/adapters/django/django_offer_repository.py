from typing import List

from checkout_backend.entities.offer_entity import OfferEntity
from checkout_backend.interfaces.offer_repository import OfferRepository
from checkout_backend.models import Offer


class DjangoOfferRepository(OfferRepository):

    def update_or_create(self, product_code: str, defaults: dict) -> OfferEntity:
        offer, created = Offer.objects.update_or_create(
            product__code=product_code,
            defaults=defaults,
        )

        return offer.to_entity()

    def all(self) -> List[OfferEntity]:
        return [offer.to_entity() for offer in Offer.objects.all()]
