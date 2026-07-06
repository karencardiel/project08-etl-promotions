import pandas as pd
import logging

def extract_data(engine):

    logging.info("EXTRACT STAGE")

    analytics = pd.read_sql(
        "SELECT * FROM analytics;",
        engine
    )

    orders = pd.read_sql(
        "SELECT * FROM orders;",
        engine
    )

    order_items = pd.read_sql(
        "SELECT * FROM order_items;",
        engine
    )

    logging.info(f"Analytics rows: {len(analytics)}")
    logging.info(f"Orders rows: {len(orders)}")
    logging.info(f"Order Items rows: {len(order_items)}")

    print(f"Analytics: {len(analytics)} rows")
    print(f"Orders: {len(orders)} rows")
    print(f"Order Items: {len(order_items)} rows")

    return analytics, orders, order_items