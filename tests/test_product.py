import pytest

from src.product import Product


def test_product_init(once_product):
    assert once_product.name == "Iphone 15"
    assert once_product.description == "256GB, Gray space"
    assert once_product.price == 210000.0
    assert once_product.quantity == 4


def test_empty_name_or_description():
    product = Product("", "", 0.0, 0)
    assert product.name == ""
    assert product.description == ""
    assert product.price == 0.0
    assert product.quantity == 0


def test_update_product():
    product = Product("Old Name", "Old Description", 100.0, 10)
    product.name = "New Name"
    product.description = "New Description"
    product.price = 200.0
    product.quantity = 5

    assert product.name == "New Name"
    assert product.description == "New Description"
    assert product.price == 200.0
    assert product.quantity == 5


def test_product_price_getter_setter():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.price == 100.0
    product.price = 200.0
    assert product.price == 200.0
    product.price = -50.0
    assert product.price == 200.0


def test_new_product_creation():
    product_list = []
    product_data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 100.0,
        "quantity": 10,
    }

    new_product = Product.new_product(product_data, product_list)
    assert len(product_list) == 1
    assert new_product.name == "Test Product"
    assert new_product.description == "Test Description"
    assert new_product.price == 100.0
    assert new_product.quantity == 10


def test_new_product_duplicate_handling():
    product_list = [Product("Existing Product", "Existing Description", 150.0, 5)]

    product_data = {
        "name": "Existing Product",
        "description": "New Description",
        "price": 120.0,
        "quantity": 10,
    }

    updated_product = Product.new_product(product_data, product_list)
    assert len(product_list) == 1
    assert updated_product.name == "Existing Product"
    assert updated_product.description == "Existing Description"
    assert updated_product.price == 150.0
    assert updated_product.quantity == 15


def test_product_addition():
    product_a = Product("iPhone 15", "Смартфон", 100000.0, 10)
    product_b = Product("Samsung Galaxy S23", "Смартфон", 90000.0, 2)

    total_cost = product_a + product_b
    assert total_cost == 100000.0 * 10 + 90000.0 * 2


def test_product_addition_invalid_type():
    product_a = Product("iPhone 15", "Смартфон", 100000.0, 10)
    with pytest.raises(TypeError):
        _ = product_a + "Not a Product"


def test_product_str_representation():
    product = Product("iPhone 15", "Смартфон", 100000.0, 10)
    assert str(product) == "iPhone 15, 100000.0 руб. Остаток: 10 шт."
