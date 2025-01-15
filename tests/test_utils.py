from src.category import Category
from src.product import Product
from src.utils import objects_from_json, read_json


def test_read_json(sample_json):
    data = read_json(sample_json)
    assert isinstance(data, list)
    assert data[0]["name"] == "Смартфоны"
    assert data[0]["products"][0]["name"] == "iPhone 15"


def test_objects_from_json(sample_json):
    data = read_json(sample_json)
    categories = objects_from_json(data)

    assert len(categories) == 1
    category = categories[0]
    assert isinstance(category, Category)
    assert category.name == "Смартфоны"
    assert category.description == "Категория смартфонов"
    assert len(category.products) == 2

    product1 = category.products[0]
    product2 = category.products[1]

    assert isinstance(product1, Product)
    assert product1.name == "iPhone 15"
    assert product1.price == 210000.0
    assert product1.quantity == 8

    assert product2.name == "Samsung Galaxy S23 Ultra"
    assert product2.price == 180000.0
    assert product2.quantity == 5
