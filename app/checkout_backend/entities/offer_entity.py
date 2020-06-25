import attr

from checkout_backend.entities.product_entity import ProductEntity


@attr.s
class OfferEntity(object):
    id = attr.ib(default=None)
    name = attr.ib(type=str, default='')
    product = attr.ib(validator=attr.validators.instance_of(ProductEntity), default=None)
    quantity = attr.ib(type=int, default=0)
    discount_unit = attr.ib(type=int, default=0)
    discount_percent = attr.ib(type=int, default=0)
