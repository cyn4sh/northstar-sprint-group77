from django.urls import path
from tickets.views import OrderStatusView

urlpatterns = [
    path("orders/<str:order_id>/status/", OrderStatusView.as_view(), name="order-status"),
]
