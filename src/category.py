from src.product import Product


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.__products = products if products else []  # Список товаров (объекты Product)
        Category.category_count += 1  # Количество категорий
        Category.product_count += len(self.__products)  # Количество товаров

    @property
    def products(self):
        return self.__products

    def display_products(self):
        return [
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n" for product in self.__products
        ]

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
