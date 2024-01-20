class Promotion:
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity):
        pass


class PercentageDiscount(Promotion):
    def __init__(self, name, percentage):
        super().__init__(name)
        self.percentage = percentage

    def apply_promotion(self, product, quantity):
        return (product.price * quantity) * (1 - self.percentage)


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        if quantity % 2 == 0:
            return (product.price * quantity) * 0.75
        else:
            return ((product.price * (quantity - 1)) * 0.75) + product.price


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        if quantity % 3 == 0:
            return (product.price * quantity) * (2 / 3)
        else:
            extra_quantity = quantity % 3
            return ((product.price * (quantity - extra_quantity)) * (2 / 3)) + product.price * extra_quantity
