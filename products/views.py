from django.shortcuts import render
from application.serializers import ProductSerializer
from rest_framework import viewsets
from domain.models.products import Producto

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductSerializer


# orders/views.py

from rest_framework import viewsets
from .models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# payments/views.py

from rest_framework import viewsets
from .models import Payment


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
