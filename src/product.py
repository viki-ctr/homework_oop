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

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Сложение возможно только между объектами класса Product")
        if type(self) != type(other):
            raise TypeError("Сложение возможно только между объектами одного типа")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color