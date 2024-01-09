from django.urls import path

from products.api.products_apiview import ProductsAPIView


class Urls(object):
    urlpatterns = [
        path("products/", ProductsAPIView.as_view()),
    ]
