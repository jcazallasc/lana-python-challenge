class CartRepository:

    def create(self):
        raise NotImplementedError

    def save(self, cart):
        raise NotImplementedError

    def get(self, id: str):
        raise NotImplementedError

    def add_product(self, cart, product):
        raise NotImplementedError

    def remove_product(self, cart, product):
        raise NotImplementedError
