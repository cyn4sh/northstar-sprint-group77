from django.core.management.base import BaseCommand
from tickets.models import Product, Order, Ticket


class Command(BaseCommand):
    help = "Seeds the database with sample Product, Order, and Ticket records for demo/testing"

    def handle(self, *args, **options):
        self.stdout.write("Seeding data...")

        # Products — mix of in-stock and out-of-stock for edge-case testing
        products_data = [
            {"sku": "ABC123", "name": "Wireless Mouse", "quantity_available": 42},
            {"sku": "XYZ789", "name": "Mechanical Keyboard", "quantity_available": 15},
            {"sku": "DEF456", "name": "USB-C Hub", "quantity_available": 0},
            {"sku": "GHI321", "name": "Laptop Stand", "quantity_available": 7},
        ]
        products = {}
        for data in products_data:
            product, created = Product.objects.get_or_create(
                sku=data["sku"], defaults=data
            )
            products[data["sku"]] = product
            self.stdout.write(f"  Product {'created' if created else 'exists'}: {product.sku}")

        # Orders — mix of statuses
        orders_data = [
            {"order_id": "ORD001", "customer_name": "Jane Doe", "customer_email": "jane@example.com", "status": "pending"},
            {"order_id": "ORD002", "customer_name": "John Smith", "customer_email": "john@example.com", "status": "shipped"},
            {"order_id": "ORD003", "customer_name": "Amara Okafor", "customer_email": "amara@example.com", "status": "delivered"},
        ]
        orders = {}
        for data in orders_data:
            order, created = Order.objects.get_or_create(
                order_id=data["order_id"], defaults=data
            )
            orders[data["order_id"]] = order
            self.stdout.write(f"  Order {'created' if created else 'exists'}: {order.order_id}")

        # Tickets — a couple linked to the above, for Task 11 audit log to reference
        Ticket.objects.get_or_create(
            raw_text="Where is my order ORD001?",
            defaults={
                "category": "order_status",
                "related_order": orders["ORD001"],
                "status": "new",
            },
        )
        Ticket.objects.get_or_create(
            raw_text="Do you have the USB-C Hub in stock?",
            defaults={
                "category": "stock_availability",
                "related_product": products["DEF456"],
                "status": "new",
            },
        )

        self.stdout.write(self.style.SUCCESS("Seeding complete."))