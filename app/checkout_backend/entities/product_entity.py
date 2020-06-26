import attr

from utils.formatters import format_price


@attr.s
class ProductEntity(object):
    id = attr.ib(default=None)
    code = attr.ib(type=str, default='')
    name = attr.ib(type=str, default='')
    price = attr.ib(type=int, default=0)

    @property
    def price_formatted(self):
        return format_price(self.price)
