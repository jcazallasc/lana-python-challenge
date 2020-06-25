import attr


@attr.s
class ProductEntity(object):
    id = attr.ib(default=None)
    code = attr.ib(type=str, default='')
    name = attr.ib(type=str, default='')
    price = attr.ib(type=int, default=0)
