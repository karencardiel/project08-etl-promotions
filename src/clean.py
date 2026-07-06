import pandas as pd
import logging

def clean_data(analytics, orders, order_items):

    logging.info("CLEAN STAGE")

    # Remove duplicate rows using primary key
    analytics = analytics.drop_duplicates(subset=["id"])
    orders = orders.drop_duplicates(subset=["id"])
    order_items = order_items.drop_duplicates(subset=["id"])

    # Convert date columns
    analytics["timestamp"] = pd.to_datetime(analytics["timestamp"])
    analytics["created_at"] = pd.to_datetime(analytics["created_at"])

    orders["created_at"] = pd.to_datetime(orders["created_at"])

    logging.info("Duplicates removed.")
    logging.info("Datetime conversion completed.")

    print("Cleaning completed.")

    return analytics, orders, order_items