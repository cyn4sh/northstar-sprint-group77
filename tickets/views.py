from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as http_status
from tickets.models import Order, Product
from tickets.serializers import OrderStatusSerializer, StockAvailabilitySerializer

class OrderStatusView(APIView):
    

    def get(self, request, order_id):
        try:
            order = Order.objects.get(order_id=order_id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found."}, status=http_status.HTTP_404_NOT_FOUND)

        serializer = OrderStatusSerializer(order)
        return Response(serializer.data)

class StockAvailabilityView(APIView):
    
    def get(self, request, sku):
        try:
            product = Product.objects.get(sku=sku)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."}, status=http_status.HTTP_404_NOT_FOUND)

        serializer = StockAvailabilitySerializer(product)
        return Response(serializer.data)