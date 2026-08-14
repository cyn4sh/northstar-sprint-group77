# Go-Live Readiness Note — Northstar Sprint, Group 77

## What Works (based on GitHub issues)
- *Data Schema* (Issue #1 – Victor): Product, Order, Ticket models built and migrated to Postgres.
- *Order-Status Lookup API* (Issue #3 – Victor): GET /api/orders/<order_id>/status/ — returns order status, customer info, order date. Tested, returns 404 on invalid order ID.
- *Stock-Availability Lookup API* (Issue #4 – Victor): GET /api/products/<sku>/stock/ — returns product info + computed in_stock boolean. Tested, returns 404 on invalid SKU.
- (Add status for Tasks 2, 5, 6, 7, 8 here once confirmed by Sandra, Khalid, and Melody.)

## Known Issues / Limitations
- No classifier/router yet connecting raw ticket text to the correct endpoint (Tasks 5/6, in progress).
- No auto-response templates yet (Task 7).
- No seed/mock data pipeline yet — endpoints have only been tested against manually created shell records (Task 2).
- No authentication — out of scope for this MVP by design.
- Returns/refunds ticket type is explicitly out of scope for this MVP (team chose to cover order-status and stock-availability only).
- No frontend or chatbot — this MVP is a backend API only.

## Next Steps for Northstar Team
- Complete ticket classifier/router (Tasks 5/6) so raw tickets route to the correct endpoint.
- Build auto-response templates for each ticket category (Task 7).
- Finish seed/mock data script for repeatable testing (Task 2).
- Run edge-case testing across both endpoints (Task 8).
- Package audit log and final submission artifacts (Tasks 11, 12).
