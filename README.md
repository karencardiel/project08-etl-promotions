# Promotion Impact on Shopping Cart Behavior

ETL pipeline that analyzes whether promotions increase the probability of users adding products to the shopping cart.

## What it does

1. **Extract**: connects to a PostgreSQL database (NeonDB) and pulls data from 3 tables: `analytics`, `orders`, `order_items`.
2. **Clean**: removes duplicates and standardizes timestamps.
3. **Transform**: calculates key indicators (sessions, promo clicks, conversion rate).
4. **Load**: exports results to CSV.
5. **Visualize**: generates charts of the indicators.

## Main result

Promotion → cart conversion rate: **58.3%**

## How to run it

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file with your database credentials:

```
DATABASE_URL=postgresql://user:password@host/db
```

Then run:

```bash
python3 main.py
```
