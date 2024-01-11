from django.urls import path

from products.api.products_apiview import (
    ProductsAPIView,
    SingleProductAPIView,
    AgregarProductAPIView,
    RestoreProductView,
    ProductDetailView,
)


class Urls(object):
    urlpatterns = [
        path("api/products/", ProductsAPIView.as_view()),
        path("api/products/<int:product_id>/", SingleProductAPIView.as_view()),
        path("api/products/create/", AgregarProductAPIView.as_view()),
        path(
            "api/products/<int:id>/delete/",
            ProductDetailView.as_view(),
        ),
        path("api/products/<int:product_id>/restore/", RestoreProductView.as_view()),
    ]
