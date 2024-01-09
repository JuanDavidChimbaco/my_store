from rest_framework import serializers
from domain.models.products import Producto


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"
