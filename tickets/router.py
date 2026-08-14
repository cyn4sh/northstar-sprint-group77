"""
Task 6 — Ticket routing logic.

Takes raw ticket text, classifies it (using classifier.py), extracts
the relevant identifier (order ID, SKU, or product name), and fetches
the matching record so a response can be generated.
"""

import re

from tickets.classifier import classify_ticket
from tickets.models import Order, Product


def extract_order_id(text):
    """
    Pulls an order ID out of raw text.
    Matches patterns like 'ORD001', 'ord123', 'TEST001' —
    3+ letters followed directly by digits, no space between them.
    """
    match = re.search(r"\b([A-Za-z]{3,}\d+)\b", text)
    if match:
        return match.group(1).upper()
    return None


def extract_sku(text):
    """
    Pulls a SKU out of raw text.
    Matches patterns like 'ABC123', 'xyz789' — same shape as order IDs,
    since your SKUs and order IDs follow the same letters+digits format.
    """
    match = re.search(r"\b([A-Za-z]{3,}\d+)\b", text)
    if match:
        return match.group(1).upper()
    return None


def find_product(text):
    """
    Finds a product two ways, in order of confidence:
    1. By SKU, if the text contains something SKU-shaped (e.g. 'DEF456').
    2. By product name, if any known product's name appears in the text
       (e.g. 'USB-C Hub' inside 'Do you have the USB-C Hub in stock?').

    Returns a single Product instance, or None if nothing matches
    (either not found, or ambiguous — see notes below).
    """
    # First, try SKU — most reliable, exact match
    sku = extract_sku(text)
    if sku:
        try:
            return Product.objects.get(sku=sku)
        except Product.DoesNotExist:
            # A SKU-shaped string was found but doesn't exist —
            # don't fall through to name matching, this is a real
            # "not found" case, not a missing SKU.
            return "NOT_FOUND"

    # No SKU-shaped text found — try matching by product name instead.
    # Case-insensitive, checks if any existing product's name appears
    # anywhere in the ticket text.
    text_lower = text.lower()
    matches = [
        product for product in Product.objects.all()
        if product.name.lower() in text_lower
    ]

    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        # More than one product name appears in the text — ambiguous,
        # can't safely guess which one the customer means.
        return "AMBIGUOUS"

    return None


def route_ticket(raw_text):
    """
    Main routing function.
    1. Classifies the ticket.
    2. Extracts the relevant identifier based on category.
    3. Looks up the matching record.
    4. Returns a dict with the result, ready to be used in a response.
    """
    category = classify_ticket(raw_text)

    if category == "order_status":
        order_id = extract_order_id(raw_text)
        if not order_id:
            return {"category": category, "error": "No order ID found in ticket text"}

        try:
            order = Order.objects.get(order_id=order_id)
        except Order.DoesNotExist:
            return {"category": category, "error": f"Order {order_id} not found"}

        return {
            "category": category,
            "order_id": order.order_id,
            "customer_name": order.customer_name,
            "status": order.status,
        }

    elif category == "stock_availability":
        result = find_product(raw_text)

        if result is None:
            return {"category": category, "error": "No product SKU or name found in ticket text"}
        if result == "NOT_FOUND":
            return {"category": category, "error": "Product not found"}
        if result == "AMBIGUOUS":
            return {"category": category, "error": "Multiple matching products found — please specify SKU"}

        product = result
        return {
            "category": category,
            "sku": product.sku,
            "name": product.name,
            "in_stock": product.quantity_available > 0,
            "quantity_available": product.quantity_available,
        }

    else:
        return {"category": "unclassified", "error": "Could not classify ticket"}