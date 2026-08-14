"""
Task 8 — Tests and edge cases.

Covers the two API endpoints (order-status, stock-availability) and
the classifier/router logic (Tasks 5/6), using real seed data.

Run with: python manage.py test
"""

from django.test import TestCase
from django.urls import reverse

from tickets.models import Product, Order
from tickets.classifier import classify_ticket
from tickets.router import route_ticket


class OrderStatusEndpointTests(TestCase):
    def setUp(self):
        # Fresh, isolated test data — Django wipes this after each test,
        # so it doesn't depend on seed_data having been run.
        self.order = Order.objects.create(
            order_id="ORD001",
            customer_name="Jane Doe",
            customer_email="jane@example.com",
            status="shipped",
        )

    def test_valid_order_returns_200_and_correct_data(self):
        response = self.client.get("/api/orders/ORD001/status/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["order_id"], "ORD001")
        self.assertEqual(response.data["status"], "shipped")
        self.assertEqual(response.data["customer_name"], "Jane Doe")

    def test_invalid_order_returns_404(self):
        response = self.client.get("/api/orders/ORD999/status/")
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", response.data)


class StockAvailabilityEndpointTests(TestCase):
    def setUp(self):
        self.in_stock_product = Product.objects.create(
            sku="ABC123", name="Wireless Mouse", quantity_available=42
        )
        self.out_of_stock_product = Product.objects.create(
            sku="DEF456", name="USB-C Hub", quantity_available=0
        )

    def test_in_stock_product_returns_true(self):
        response = self.client.get("/api/products/ABC123/stock/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["in_stock"], True)
        self.assertEqual(response.data["quantity_available"], 42)

    def test_out_of_stock_product_returns_false(self):
        response = self.client.get("/api/products/DEF456/stock/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["in_stock"], False)

    def test_invalid_sku_returns_404(self):
        response = self.client.get("/api/products/ZZZ999/stock/")
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", response.data)


class ClassifierTests(TestCase):
    def test_order_status_keywords_classified_correctly(self):
        self.assertEqual(
            classify_ticket("Where is my order ORD001?"), "order_status"
        )
        self.assertEqual(
            classify_ticket("Has my package shipped yet?"), "order_status"
        )

    def test_stock_keywords_classified_correctly(self):
        self.assertEqual(
            classify_ticket("Is this back in stock?"), "stock_availability"
        )
        self.assertEqual(
            classify_ticket("Do you have this available?"), "stock_availability"
        )

    def test_unrelated_text_is_unclassified(self):
        self.assertEqual(
            classify_ticket("What's your refund policy?"), "unclassified"
        )


class RouterTests(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            order_id="ORD001",
            customer_name="Jane Doe",
            customer_email="jane@example.com",
            status="pending",
        )
        self.product = Product.objects.create(
            sku="DEF456", name="USB-C Hub", quantity_available=0
        )

    def test_route_order_status_by_id(self):
        result = route_ticket("Where is my order ORD001?")
        self.assertEqual(result["category"], "order_status")
        self.assertEqual(result["order_id"], "ORD001")
        self.assertEqual(result["status"], "pending")

    def test_route_order_not_found(self):
        result = route_ticket("Where is my order ORD999?")
        self.assertEqual(result["category"], "order_status")
        self.assertIn("error", result)

    def test_route_stock_by_sku(self):
        result = route_ticket("Do you have DEF456 in stock?")
        self.assertEqual(result["category"], "stock_availability")
        self.assertEqual(result["sku"], "DEF456")

    def test_route_stock_by_product_name(self):
        result = route_ticket("Do you have the USB-C Hub in stock?")
        self.assertEqual(result["category"], "stock_availability")
        self.assertEqual(result["sku"], "DEF456")

    def test_route_unclassified_ticket(self):
        result = route_ticket("What's your refund policy?")
        self.assertEqual(result["category"], "unclassified")
        self.assertIn("error", result)