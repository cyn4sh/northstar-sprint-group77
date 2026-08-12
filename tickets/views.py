from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as http_status
from tickets.models import Order
from tickets.serializers import OrderStatusSerializer

class OrderStatusView(APIView):
    

    def get(self, request, order_id):
        try:
            order = Order.objects.get(order_id=order_id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found."}, status=http_status.HTTP_404_NOT_FOUND)

        serializer = OrderStatusSerializer(order)
        return Response(serializer.data)