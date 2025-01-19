class Product:
    """Класс для описания продуктов"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name  # Название товара
        self.description = description  # Описание товара
        self.__price = price  # Цена товара (с плавающей точкой для копеек)
        self.quantity = quantity  # Количество в наличии (целое число)

    @classmethod
    def new_product(cls, product_data: dict, product_list: list):
        for product in product_list:
            if product.name == product_data["name"]:
                product.quantity += product_data["quantity"]
                product.price = max(product.price, product_data["price"])
                return product
        new_product = cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )
        product_list.append(new_product)
        return new_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)
