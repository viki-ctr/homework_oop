from src.product import Product
from src.product import Smartphone
from src.product import LawnGrass


def test_print_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава 2, Выносливая трава, 450.0, 15)"