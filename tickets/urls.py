from django.urls import path
from tickets.views import OrderStatusView, StockAvailabilityView

urlpatterns = [
    path("orders/<str:order_id>/status/", OrderStatusView.as_view(), name="order-status"),
    path("products/<str:sku>/stock/", StockAvailabilityView.as_view(), name="stock-availability"),
]
