from rest_framework import serializers
from products.domain.models.products import Producto, Talla, Color, Categoria


class TallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talla
        fields = "__all__"


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    tallas = TallaSerializer(many=True)
    colores = ColorSerializer(many=True)
    categoria = CategoriaSerializer()

    class Meta:
        model = Producto
        fields = "__all__"
