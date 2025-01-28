from src.base_product import BaseProduct
from src.product import Product
import pytest


def test_abstract_class_instantiation():
    with pytest.raises(TypeError):
        BaseProduct()


def test_product_inherits_base_product():
    product = Product("Example Product", "Example Description", 100.0, 10)
    assert isinstance(product, BaseProduct)
    assert isinstance(product, Product)
