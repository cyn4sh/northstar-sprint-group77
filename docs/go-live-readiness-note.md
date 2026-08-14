# Go-Live Readiness Note — Northstar Sprint, Group 77

## What Works (based on GitHub issues)
- **Data Schema** (Issue #1 – Victor): Product, Order, Ticket models built and migrated to Postgres.
- **Order-Status Lookup API** (Issue #3 – Victor): `GET /api/orders/<order_id>/status/` — returns order status, customer info, order date. Tested, returns 404 on invalid order ID.
- **Stock-Availability Lookup API** (Issue #4 – Victor): `GET /api/products/<sku>/stock/` — returns product info + computed `in_stock` boolean. Tested, returns 404 on invalid SKU.
- **Seed Data** (Issue #2 – Victor): custom `seed_data` management command populates sample Products, Orders, and Tickets via `python manage.py seed_data`. Idempotent, safe to re-run.
- **Ticket Classifier** (Khalid): rule-based intent classifier — detects `order_status`, `stock_availability`, or `unclassified` from raw ticket text.
- **Ticket Routing** (Khalid): extracts order ID or SKU/product name from ticket text and fetches the matching record, with explicit handling for not-found and ambiguous matches.
- **Tests** (Khalid): unit tests covering both endpoints, the classifier, and the router — 13 tests, all passing.
- **Auto-Response Templates** (Melody): response templates for order-status, stock-availability, and unclassified ticket categories, mapped to real model fields.

## Known Issues / Limitations
- Product lookup by name only works via exact/partial name match — no fuzzy matching or typo tolerance.
- No authentication — out of scope for this MVP by design.
- Returns/refunds ticket type is explicitly out of scope for this MVP (team chose to cover order-status and stock-availability only).
- No frontend or chatbot — this MVP is a backend API only.

## Next Steps for Northstar Team
- Package audit log and final submission artifacts (Tasks 11, 12).

*Note: This note reflects the verified state of the repo's commit history and GitHub issues as of sprint delivery.*