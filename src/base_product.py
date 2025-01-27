from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Создан базовый абстрактный класс"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
