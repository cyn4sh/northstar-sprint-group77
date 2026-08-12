from rest_framework import serializers
from tickets.models import Order

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["order_id", "customer_name", "customer_email", "status", "order_date"]