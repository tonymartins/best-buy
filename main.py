import store
import products

# setup initial stock of inventory
# setup initial stock of inventory
product_list = [
                products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                products.NonStockedProduct("Windows License", price=125),
                products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]
best_buy = store.Store(product_list)


def print_separator():
    print("------")


def list_all_products(products_store):
    existent_products = products_store.get_all_products()
    print_separator()
    for count, product in enumerate(existent_products):
        details = product.show()
        print(f'{count + 1}. {details}')


def show_total_amount(products_store):
    existent_products = products_store.get_all_products()
    total_amount = 0
    for product in existent_products:
        total_amount += product.quantity
    print_separator()
    print(f'Total of {total_amount} items in store')


def make_order(products_store):
    list_all_products(products_store)
    existent_products = products_store.get_all_products()
    order_list = []
    order_is_open = True
    while order_is_open:
        print_separator()
        print('When you want to finish the order, enter empty text.')
        product_choice = input('Which product # do you want? ')
        product_amount = input('What amount do you want? ')
        if product_choice == "":
            order_is_open = False
        elif int(product_choice) - 1 in range(len(existent_products)):
            product_index = int(product_choice) - 1
            order_list.append((existent_products[product_index], int(product_amount)))
        else:
            print("Error adding product!")
    order_total = products_store.order(order_list)
    print(f'Order made! Total payment: ${order_total}')


def start(products_store):
    user_choice = input("""
----------
Store Menu
----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
Please choose a number: """)
    # Choose functionality based on user input
    if user_choice == "1":
        list_all_products(products_store)
    if user_choice == "2":
        show_total_amount(products_store)
    if user_choice == "3":
        make_order(products_store)
    if user_choice == "4":
        exit()
    # Loop
    start(best_buy)


if __name__ == "__main__":
    start(best_buy)
