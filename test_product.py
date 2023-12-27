import pytest
import products
import store


def test_product_normal():
    assert products.Product("Mac", price=100, quantity=1000)


def test_product_invalid_name():
    with pytest.raises(Exception):
        products.Product("", price=100, quantity=1000)


def test_product_invalid_price():
    with pytest.raises(Exception):
        products.Product("Mac", price=-1, quantity=1000)


def test_product_zero_quantity_():
    test_product = products.Product("Mac", price=100, quantity=10)
    test_store = store.Store([test_product])
    test_store.order([(test_product, 10)])
    assert test_product.active is False


def test_product_modifies_quantity():
    test_product = products.Product("Mac", price=100, quantity=10)
    initial_quantity = test_product.quantity
    test_store = store.Store([test_product])
    test_store.order([(test_product, 5)])
    final_quantity = test_product.quantity
    assert initial_quantity != final_quantity


def test_buy_too_much_quantity():
    test_product = products.Product("Mac", price=100, quantity=1)
    test_store = store.Store([test_product])
    with pytest.raises(Exception):
        test_store.order([(test_product, 10)])


pytest.main()
