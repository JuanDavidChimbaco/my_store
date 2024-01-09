from abc import ABC, abstractmethod


class ProductsRepository(ABC):
    @abstractmethod
    def get_products(self):
        pass
