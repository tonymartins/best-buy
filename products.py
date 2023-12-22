class Product:
    def __init__(self, name, price=0, quantity=0):
        self.active = True
        if name != "" and price >= 0 and quantity >= 0:
            self.name = name
            self.price = price
            self.quantity = quantity
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

    def buy(self, quantity):
        self.quantity -= quantity
        return quantity * self.price
