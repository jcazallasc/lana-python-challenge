from typing import List

from checkout_backend.interfaces.offer_repository import OfferRepository
from checkout_backend.models import Offer


class DjangoOfferRepository(OfferRepository):

    def all(self) -> List[Offer]:
        return Offer.objects.all()
