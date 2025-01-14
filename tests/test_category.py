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
    category.add_product(product)

    assert len(category.products) == 1
    assert category.products[0] == product
    assert Category.product_count == initial_product_count + 1


def test_category_without_products():
    category = Category("Empty Category", "No products here")

    assert category.name == "Empty Category"
    assert category.description == "No products here"
    assert len(category.products) == 0


def test_no_duplicate_products():
    product = Product("Unique Product", "Description", 50.0, 2)
    category = Category("Category", "Description", [product])
    category.add_product(product)
    assert len(category.products) == 2


def test_empty_category():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Empty", "No products")
    assert len(category.products) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0
