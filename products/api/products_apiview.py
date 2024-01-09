from rest_framework.response import Response
from rest_framework.views import APIView

from products.adapter.products_repository_adapter import ProductsRepositoryAdapter
from application.serializers import ProductSerializer
from usecases.get_products import GetFilteredProducts, GetProducts


class ProductsAPIView(APIView):
    def get(self, request):
        get_products = GetProducts(ProductsRepositoryAdapter())
        products = get_products.execute()

        # Obtiene los parámetros de la consulta
        name = request.query_params.get("name", None)
        price_from = request.query_params.get("price_from", None)
        price_to = request.query_params.get("price_to", None)

        # Ejecuta el caso de uso
        get_filtered_products = GetFilteredProducts(ProductsRepositoryAdapter())
        page_obj = get_filtered_products.execute(name, price_from, price_to)

        serializer = ProductSerializer(page_obj, products, many=True)
        return Response(serializer.data)
