import pytest

from src.category import Category
from src.product import Product


def test_once_category(first_category):
    assert first_category.name == "Телевизоры"
    assert (
        first_category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert first_category.category_count == 1
    assert first_category.product_count == 1


def test_with_two_product(any_product_in_categories):
    assert any_product_in_categories.name == "Смартфоны"
    assert (
        any_product_in_categories.description
        == "Смартфоны - средство получения дополнительных функций для удобства жизни"
    )
    assert any_product_in_categories.category_count == 1
    assert any_product_in_categories.product_count == 2


def test_add_product_to_category():
    product = Product("Test Product", "Test Description", 100.0, 10)
    category = Category("Test Category", "Test Description")

    initial_product_count = Category.product_count
    category.add_product = product

    assert "Test Product, 100.0 руб. Остаток: 10 шт.\n"
    assert Category.product_count + 1 == initial_product_count + 1


def test_category_without_products():
    category = Category("Empty Category", "No products here")

    assert category.name == "Empty Category"
    assert category.description == "No products here"
    assert len(category.products) == 0


def test_no_duplicate_products():
    product = Product("Unique Product", "Description", 50.0, 2)
    category = Category("Category", "Description", [product])
    category.add_product = product
    assert len(category.products) == 1
    assert category.products.count('"Unique Product", 50.0 руб. Остаток: 2 шт.\n') == 0


def test_empty_category():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Empty", "No products")
    assert len(category.products) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_add_product_invalid_type():
    category = Category("Tools", "Hardware and tools")
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product"):
        category.add_product("Not a Product")


def test_display_products():
    product1 = Product("Smartphone", "High-end smartphone", 70000.0, 10)
    product2 = Product("Laptop", "Gaming laptop", 120000.0, 5)

    category = Category("Electronics", "Gadgets and devices", [product1, product2])

    displayed_products = category.display_products()

    expected_display = ["Smartphone, 70000.0 руб. Остаток: 10 шт.\n", "Laptop, 120000.0 руб. Остаток: 5 шт.\n"]

    assert displayed_products == expected_display


def test_product_count_across_categories():
    category1 = Category("Clothing", "Fashion items")
    category2 = Category("Accessories", "Bags and jewelry")

    product1 = Product("T-shirt", "Cotton t-shirt", 1000.0, 50)
    product2 = Product("Bag", "Leather bag", 5000.0, 15)

    initial_product_count = Category.product_count

    category1.add_product(product1)
    category2.add_product(product2)

    assert Category.product_count == initial_product_count + 2


def test_category_str():
    product1 = Product("iPhone 15", "Смартфон", 100000.0, 10)
    product2 = Product("Samsung Galaxy S23", "Смартфон", 90000.0, 5)
    category = Category("Смартфоны", "Категория смартфонов", [product1, product2])

    assert str(category) == "Смартфоны, количество продуктов: 15 шт."
