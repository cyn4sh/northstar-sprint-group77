# Northstar Sprint — Group 77

Support Deflection MVP for Northstar Retail Co., built as part of the PLP 1MILL Devs Software Engineering Programme (Week 1: Northstar Sprint).

## Project Overview
Northstar Retail Co.'s support team is overwhelmed by repetitive tickets across three categories: order-status, returns/refunds, and stock-availability. This MVP addresses **order-status** and **stock-availability** via a backend API that lookups can be built against — reducing manual ticket handling without needing a full product.

See [`CHARTER.md`](./CHARTER.md) for team norms, communication rules, and escalation process.

## Tech Stack
- Python / Django
- Django REST Framework (DRF)
- PostgreSQL
- drf-spectacular (API schema)

## Setup

1. Clone the repo and enter the project folder:
   ```
   git clone https://github.com/cyn4sh/northstar-sprint-group77.git
   cd northstar_sprint
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/Scripts/activate   # Git Bash on Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file (see `.env.example` if present) with your local Postgres credentials.

5. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the server:
   ```
   python manage.py runserver
   ```

## API Endpoints

### Order Status
```
GET /api/orders/<order_id>/status/
```
Returns the order's status, customer info, and order date. Returns `404` if the order doesn't exist.

**Example response:**
```json
{
    "order_id": "TEST001",
    "customer_name": "Jane Doe",
    "customer_email": "jane@example.com",
    "status": "shipped",
    "order_date": "2026-08-12T21:44:25.540470Z"
}
```

### Stock Availability
```
GET /api/products/<sku>/stock/
```
Returns product info and a computed `in_stock` boolean based on `quantity_available`. Returns `404` if the product doesn't exist.

**Example response:**
```json
{
    "sku": "ABC123",
    "name": "Wireless Mouse",
    "quantity_available": 15,
    "in_stock": true
}
```

## Board & Task Tracking
Task ownership, priority, and Definition of Done are tracked on the [GitHub Project board](../../projects) — "Northstar Sprint - Group 77".

## Team
- Victor Ojo (Ashfall) — Group Lead
- Khalid Swaleh
- Sandra Koech
- Demeke Yeshanew
- Melody Mmbone