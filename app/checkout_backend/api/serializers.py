from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.CharField()
    code = serializers.CharField()
    name = serializers.CharField()
    price = serializers.CharField()

class CartItemSerializer(serializers.Serializer):
    product = ProductSerializer()
    quantity = serializers.CharField()

class CartSerializer(serializers.Serializer):
    id = serializers.CharField()
    items = CartItemSerializer(many=True)

class CheckoutSerializer(serializers.Serializer):
    cart = CartSerializer()
    total_amount = serializers.CharField()
