from django.urls import path

from checkout_frontend.views import CheckoutView

urlpatterns = [
    path(
        '',
        CheckoutView().get,
        name='checkout',
    ),
]
