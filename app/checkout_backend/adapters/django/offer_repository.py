from typing import List

from checkout_backend.entities.offer_entity import OfferEntity
from checkout_backend.entities.product_entity import ProductEntity
from checkout_backend.interfaces.offer_repository import OfferRepository
from checkout_backend.models import Offer


class DjangoOfferRepository(OfferRepository):

    def update_or_create(self, product: ProductEntity, defaults: dict) -> OfferEntity:
        offer, created = Offer.objects.update_or_create(
            product_id=product.id,
            defaults=defaults,
        )

        return offer.to_entity()

    def all(self) -> List[OfferEntity]:
        return [offer.to_entity() for offer in Offer.objects.all()]
