from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from checkout_backend.api.serializers import CheckoutSerializer
from checkout_backend.app import app
from checkout_backend.uses_cases.checkout import Checkout


class CreateCartAPIView(APIView):

    def post(self, request,):
        cart_entity = app.checkout.create_cart()

        serializer = CheckoutSerializer({
            'cart': {
                'id': cart_entity.id,
                'items': app.checkout.get_items(cart_entity.id),
            },
            'total_amount': app.checkout.get_total_amount(cart_entity),
        })

        return Response(serializer.data)

class DeleteCartAPIView(APIView):

    def delete(
        self,
        request,
        cart_id,
    ):
        app.checkout.delete_cart(cart_id)

        return Response()


class CartAddProductAPIView(APIView):

    def post(
        self,
        request,
        cart_id,
        product_code,
    ):
        cart_entity = app.checkout.add_product(cart_id, product_code)

        serializer = CheckoutSerializer({
            'cart': {
                'id': cart_entity.id,
                'items': app.checkout.get_items(cart_entity.id),
            },
            'total_amount': app.checkout.get_total_amount(cart_entity),
        })

        return Response(serializer.data)

class CartRemoveProductAPIView(APIView):

    def delete(
        self,
        request,
        cart_id,
        product_code,
    ):
        cart_entity = app.checkout.remove_product(cart_id, product_code)

        serializer = CheckoutSerializer({
            'cart': {
                'id': cart_entity.id,
                'items': app.checkout.get_items(cart_entity.id),
            },
            'total_amount': app.checkout.get_total_amount(cart_entity),
        })

        return Response(serializer.data)
