from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    quantity_available = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.sku} - {self.name}"


class Order(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
    )

    order_id = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.customer_name}"


class Ticket(models.Model):
    CATEGORY_CHOICES = (
        ("order_status", "Order Status"),
        ("stock_availability", "Stock Availability"),
        ("unclassified", "Unclassified"),
    )
    STATUS_CHOICES = (
        ("new", "New"),
        ("resolved", "Resolved"),
    )

    raw_text = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="unclassified")
    related_order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    related_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket #{self.pk} - {self.category}"