from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from checkout_backend.api.serializers import CheckoutSerializer
from checkout_backend.app import app


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
        try:
            app.checkout.delete_cart(cart_id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response()


class CartAddProductAPIView(APIView):

    def post(
        self,
        request,
        cart_id,
        product_code,
    ):
        try:
            cart_entity = app.checkout.add_product(cart_id, product_code)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

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
        try:
            cart_entity = app.checkout.remove_product(cart_id, product_code)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CheckoutSerializer({
            'cart': {
                'id': cart_entity.id,
                'items': app.checkout.get_items(cart_entity.id),
            },
            'total_amount': app.checkout.get_total_amount(cart_entity),
        })

        return Response(serializer.data)
