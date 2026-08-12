from rest_framework import serializers
from tickets.models import Order, Product

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["order_id", "customer_name", "customer_email", "status", "order_date"]

class StockAvailabilitySerializer(serializers.ModelSerializer):
    in_stock = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ["sku", "name", "quantity_available", "in_stock"]

    def get_in_stock(self, obj):
        return obj.quantity_available > 0