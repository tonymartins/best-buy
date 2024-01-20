class Product:
    def __init__(self, name, price=0, quantity=0):
        self.active = True
        if name != "" and price >= 0 and quantity >= 0:
            self.name = name
            self.price = price
            self.quantity = quantity
            if self.quantity == 0:
                self.deactivate()
        else:
            raise Exception("Something went wrong.\nTry Again.")

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f'{self.name}, Price: {str(self.price)}, Quantity: {str(self.quantity)}'

    # Change the functionality according to this
    def buy(self, quantity):
        self.quantity -= quantity
        return quantity * self.price


class NonStockedProduct(Product):
    def __init__(self, name, price=0, quantity=0):
        super().__init__(name, price, quantity)
        self.activate()

    def show(self):
        return f'{self.name}, Price: {str(self.price)}, Quantity: {str(self.quantity)}'


class LimitedProduct(Product):
    def __init__(self, name, price=0, quantity=0, maximum=1):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        return f'{self.name}, Price: {str(self.price)}, Quantity: {str(self.quantity)}'
