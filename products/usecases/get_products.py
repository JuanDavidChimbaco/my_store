from products.ports.products_repository import ProductsRepository
from django.core.paginator import Paginator


class GetProducts(object):
    def __init__(self, products_repository: ProductsRepository):
        self.products_repository = products_repository

    def execute(self):
        return self.products_repository.obtener_todos_los_productos()


class GetFilteredProducts(object):
    def __init__(self, products_repository: ProductsRepository):
        self.products_repository = products_repository

    def execute(self, name=None, price_from=None, price_to=None):
        # Filtra los productos según los parámetros
        products = self.products_repository.obtener_todos_los_productos()
        if name:
            products = products.filter(name__icontains=name)
        if price_from:
            products = products.filter(price__gte=price_from)
        if price_to:
            products = products.filter(price__lte=price_to)

        # Pagina los productos
        paginator = Paginator(products, 10)
        page_obj = paginator.get_page(1)

        return page_obj


class GetProductById(object):
    def __init__(self, products_repository):
        self.products_repository = products_repository

    def execute(self, product_id):
        # Obtiene un solo producto por ID
        product = self.products_repository.get_product_by_id(product_id)
        return product
