from abc import ABC, abstractmethod
from typing import List
from products.domain.models.products import Producto


class ProductsRepository(ABC):
    @abstractmethod
    def obtener_producto_por_id(self, producto_id: int) -> Producto:
        pass

    @abstractmethod
    def obtener_todos_los_productos(self) -> List[Producto]:
        pass

    @abstractmethod
    def crear_producto(self, producto_data: dict) -> Producto:
        pass

    @abstractmethod
    def actualizar_producto(self, producto_id: int, producto_data: dict) -> Producto:
        pass

    @abstractmethod
    def eliminar_producto(self, producto_id: int):
        pass
