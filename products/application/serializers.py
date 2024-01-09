from rest_framework import serializers
from domain.models.products import Producto


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"


# class ProductSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(required=True)
#     price = serializers.DecimalField(required=True)

#     class Meta:
#         model = Product
#         fields = ("name", "price")
