from django.db.models import QuerySet
from domain.models import Producto
from products.ports.products_repository import ProductsRepository


class ProductsRepositoryAdapter(ProductsRepository):
    def __init__(self):
        self.products = Producto.objects.all()

    def get_products(self):
        return self.products
