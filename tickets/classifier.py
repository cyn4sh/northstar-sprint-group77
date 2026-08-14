"""
Task 5 — Rule-based intent classifier.

Takes raw ticket text and determines which category it belongs to,
based on keyword matching. No ML — just pattern matching, appropriate
for this MVP's scope.
"""


def classify_ticket(raw_text):
    """
    Classifies a ticket's raw text into one of three categories:
    'order_status', 'stock_availability', or 'unclassified'.

    Matches Ticket.CATEGORY_CHOICES in models.py exactly.
    """
    # Normalize text to lowercase so matching isn't case-sensitive
    # (e.g. "Order" and "order" should both match)
    text = raw_text.lower()

    # Keywords that suggest the customer is asking about an order's status
    order_status_keywords = [
        "order", "shipped", "shipping", "delivery", "delivered",
        "status", "tracking", "when will", "arrive",
    ]

    # Keywords that suggest the customer is asking about stock/availability
    stock_keywords = [
        "stock", "available", "availability", "in stock",
        "out of stock", "restock", "have any",
    ]

    # Check order-status keywords first
    for keyword in order_status_keywords:
        if keyword in text:
            return "order_status"

    # Then check stock-availability keywords
    for keyword in stock_keywords:
        if keyword in text:
            return "stock_availability"

    # If nothing matched either list, it's unclassified
    return "unclassified"