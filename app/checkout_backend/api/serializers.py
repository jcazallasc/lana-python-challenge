from rest_framework import serializers

from utils.formatters import format_price


class ProductSerializer(serializers.Serializer):
    id = serializers.CharField()
    code = serializers.CharField()
    name = serializers.CharField()
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        return format_price(obj.price)


class CartItemSerializer(serializers.Serializer):
    product = ProductSerializer()
    quantity = serializers.CharField()

class CartSerializer(serializers.Serializer):
    id = serializers.CharField()
    items = CartItemSerializer(many=True)

class CheckoutSerializer(serializers.Serializer):
    cart = CartSerializer()
    total_amount = serializers.SerializerMethodField()

    def get_total_amount(self, obj):
        return format_price(obj['total_amount'])
