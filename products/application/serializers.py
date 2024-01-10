from rest_framework import serializers
from products.domain.models.products import Producto


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"
