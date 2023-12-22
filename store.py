class Store:
    def __init__(self, product_list):
        self.list_of_products = product_list

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        self.list_of_products.remove(product)

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.list_of_products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        all_products = []
        for product in self.list_of_products:
            if product.active:
                all_products.append(product)
        return all_products

    def order(self, shopping_list):
        total_price = 0
        for item in shopping_list:
            total_price += (item[0].price * item[1])
            item[0].quantity -= item[1]
        return total_price
