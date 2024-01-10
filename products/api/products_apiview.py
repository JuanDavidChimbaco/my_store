from rest_framework.response import Response
from rest_framework.views import APIView

from products.adapter.products_repository_adapter import ProductsRepositoryAdapter
from products.application.serializers import ProductSerializer
from products.usecases.get_products import (
    GetFilteredProducts,
    GetProducts,
    GetProductById,
)


class ProductsAPIView(APIView):
    def get(self, request):
        # Obtiene los parámetros de la consulta
        name = request.query_params.get("name", None)
        price_from = request.query_params.get("price_from", None)
        price_to = request.query_params.get("price_to", None)

        # Ejecuta el caso de uso para obtener productos filtrados
        get_filtered_products = GetFilteredProducts(ProductsRepositoryAdapter())
        page_obj = get_filtered_products.execute(name, price_from, price_to)

        # Serializa los datos obtenidos del caso de uso
        serializer = ProductSerializer(page_obj, many=True)  # Usa solo page_obj aquí

        return Response(serializer.data)


class SingleProductAPIView(APIView):
    def get(self, request, product_id):
        # Ejecuta el caso de uso para obtener un solo producto por ID
        get_product_by_id = GetProductById(ProductsRepositoryAdapter())
        product = get_product_by_id.execute(product_id)

        # Serializa los datos obtenidos del caso de uso
        serializer = ProductSerializer(product)

        return Response(serializer.data)
