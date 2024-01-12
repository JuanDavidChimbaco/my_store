from typing import List
from django.db.models import QuerySet
from products.domain.models.products import Producto
from products.ports.products_repository import ProductsRepository


class ProductsRepositoryAdapter(ProductsRepository):
    def obtener_producto_por_id(self, producto_id: int) -> Producto:
        try:
            return Producto.objects.get(pk=producto_id, eliminado=False)
        except Producto.DoesNotExist:
            return None

    def obtener_todos_los_productos(self) -> List[Producto]:
        return Producto.objects.filter(eliminado=False)

    def crear_producto(self, producto_data: dict) -> Producto:
        nuevo_producto = Producto.objects.create(**producto_data)
        return nuevo_producto

    def actualizar_producto(self, producto_id: int, producto_data: dict) -> Producto:
        producto = self.obtener_producto_por_id(producto_id)
        if producto:
            for key, value in producto_data.items():
                setattr(producto, key, value)
            producto.save()
        return producto

    def eliminar_producto(self, producto_id: int):
        producto = self.obtener_producto_por_id(producto_id)
        if producto:
            producto.soft_delete()
