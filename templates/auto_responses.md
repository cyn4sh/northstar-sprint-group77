# Support Ticket Auto-Response Templates

## 1. Order Status Queries
**Triggers:** "Where is my order?", "Has this shipped yet?"

**Response Template:**
> "Hi {{customer_name}}, thanks for reaching out! Your order **#{{order_id}}** is currently **{{status}}**. Let us know if you need anything else!"

*(Maps to Order model fields: `order_id`, `status`)*

## 2. Stock Availability Queries
**Triggers:** "Is this back in stock?", "Do you have this item available?"

**Response Template — in stock:**
> "Hello! **{{name}}** (SKU: {{sku}}) is currently in stock — **{{quantity_available}}** units available."

**Response Template — out of stock:**
> "Hello! **{{name}}** (SKU: {{sku}}) is currently out of stock. We'll update our listings as soon as more becomes available."

*(Maps to Product model fields: `name`, `sku`, `quantity_available`, computed `in_stock`)*

## 3. Unclassified / Other Queries
**Triggers:** anything that doesn't match order-status or stock-availability (e.g. returns, refunds, general questions).

**Response Template:**
> "Hi {{customer_name}}, thanks for reaching out. This request needs a closer look from our support team — we've logged your ticket and someone will follow up shortly."

## Notes
- Returns/refunds are out of scope for this MVP — the "Unclassified" template above is the fallback for any ticket outside order-status and stock-availability.
- All fields referenced above exist on the actual `Order` and `Product` models — no invented fields (e.g. no tracking links, restock dates, or size variants, since none of these exist in the current schema).
