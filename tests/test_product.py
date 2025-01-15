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
