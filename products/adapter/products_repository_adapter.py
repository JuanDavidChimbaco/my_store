from django.db.models import QuerySet
from products.domain.models.products import Producto
from products.ports.products_repository import ProductsRepository


class ProductsRepositoryAdapter(ProductsRepository):
    def __init__(self):
        self.products = Producto.objects.all()

    def get_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        try:
            return Producto.objects.get(id=product_id)
        except Producto.DoesNotExist:
            return None
