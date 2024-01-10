from django.urls import path

from products.api.products_apiview import ProductsAPIView, SingleProductAPIView


class Urls(object):
    urlpatterns = [
        path("api/products/", ProductsAPIView.as_view()),
        path("api/products/<int:product_id>/", SingleProductAPIView.as_view()),
    ]
