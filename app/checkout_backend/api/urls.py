from django.urls import path

from checkout_backend.api.views import (CartAddProductAPIView, CartRemoveProductAPIView, CreateCartAPIView,
                                        DeleteCartAPIView)

urlpatterns = [
    path(
        'cart/',
        CreateCartAPIView.as_view(),
        name='create-cart',
    ),
    path(
        'cart/<str:cart_id>/delete/',
        DeleteCartAPIView.as_view(),
        name='delete-cart',
    ),
    path(
        'cart/<str:cart_id>/add-product/<str:product_code>/',
        CartAddProductAPIView.as_view(),
        name='cart-add-product',
    ),
    path(
        'cart/<str:cart_id>/remove-product/<str:product_code>/',
        CartRemoveProductAPIView.as_view(),
        name='cart-remove-product',
    ),
]
