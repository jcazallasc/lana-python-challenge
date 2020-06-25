import attr


@attr.s
class CartEntity(object):
    id = attr.ib(default=None)
    items = attr.ib(type=dict, default={})
