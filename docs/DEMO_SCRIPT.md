# MVP End-to-End Demo Script

## Overview
This script outlines the step-by-step walkthrough for presentation day, covering the two ticket types this MVP supports: order-status and stock-availability.

## Presentation Steps

### 1. Order Status Check
- **Presenter:** "First, we'll demonstrate the order-status lookup endpoint."
- **Action:** Send a `GET` request to `/api/orders/<order_id>/status/` with a valid order ID (e.g. `ORD001`).
- **Expected Result:** API returns the order's `order_id`, `customer_name`, `customer_email`, `status`, and `order_date` as JSON, with a `200 OK` response.

### 2. Stock Availability Check
- **Presenter:** "Next, we'll check stock availability for a product."
- **Action:** Send a `GET` request to `/api/products/<sku>/stock/` with a valid SKU (e.g. `ABC123`).
- **Expected Result:** API returns the product's `sku`, `name`, `quantity_available`, and a computed `in_stock` boolean, with a `200 OK` response.

### 3. Edge Case Handling — Invalid Order ID
- **Presenter:** "Now, here's our error handling for an order that doesn't exist."
- **Action:** Send a `GET` request to `/api/orders/<order_id>/status/` with an invalid order ID (e.g. `ORD999`).
- **Expected Result:** API returns `404 Not Found` with a clear `{"error": "Order not found"}` message.

### 4. Edge Case Handling — Invalid SKU
- **Presenter:** "Same handling applies for a product that doesn't exist."
- **Action:** Send a `GET` request to `/api/products/<sku>/stock/` with an invalid SKU (e.g. `XYZ999`).
- **Expected Result:** API returns `404 Not Found` with a clear `{"error": "Product not found"}` message.

## Notes
- This MVP covers order-status and stock-availability only. Returns/refunds are out of scope for this sprint.
- No chatbot or frontend UI exists — this is a backend API, demoed via browser or a tool like Postman/curl.