import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def once_product():
    return Product("Iphone 15", "256GB, Gray space", 210000.0, 4)


@pytest.fixture
def any_product_in_categories():
    Category.category_count = 0
    Category.product_count = 0
    first_product = Product("55\" QLED 4K", "Фоновая подсветка", 149000.0, 5)
    second_product = Product("Iphone XR", "256GB, Blue", 90000.0, 1)
    category = Category("Смартфоны",
                        "Смартфоны - средство получения дополнительных функций для удобства жизни",
                        [first_product, second_product])
    return category


@pytest.fixture
def first_category():
    Category.category_count = 0
    Category.product_count = 0
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [Product("Iphone 15", "512GB, Gray space", 210000.0, 8)])