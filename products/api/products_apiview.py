from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from products.domain.models.products import Producto
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


class AgregarProductAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.filter(eliminado=False)
    serializer_class = ProductSerializer
    lookup_field = "id"

    def perform_destroy(self, instance):
        instance.soft_delete()


class RestoreProductView(APIView):
    def post(self, request, product_id):
        try:
            product = Producto.objects.get(id=product_id, eliminado=True)
            product.eliminado = False
            product.save()
            return Response(
                {"message": "Producto restaurado correctamente."},
                status=status.HTTP_200_OK,
            )
        except Producto.DoesNotExist:
            return Response(
                {"error": "Producto no encontrado o no eliminado."},
                status=status.HTTP_404_NOT_FOUND,
            )
