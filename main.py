from src.extract import extract_data
from src.clean import clean_data
from src.transform import transform_data
from src.load import load_data
from src.visualize import create_graphs

from sqlalchemy import create_engine
from dotenv import load_dotenv

import os
import logging

# ==========================
# LOGGING SETUP
# ==========================
logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Pipeline started")

# ==========================
# LOAD ENV VARIABLES
# ==========================
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

# ==========================
# EXTRACT
# ==========================
logging.info("Starting extraction")

analytics, orders, order_items = extract_data(engine)

print("\n----- DATA SHAPE -----")
print(f"Analytics: {analytics.shape}")
print(f"Orders: {orders.shape}")
print(f"Order Items: {order_items.shape}")

print("\n----- ANALYTICS COLUMNS -----")
print(analytics.columns.tolist())

print("\n----- ORDERS COLUMNS -----")
print(orders.columns.tolist())

print("\n----- ORDER_ITEMS COLUMNS -----")
print(order_items.columns.tolist())

logging.info("Extraction completed")

# ==========================
# CLEAN
# ==========================
logging.info("Starting cleaning stage")

analytics, orders, order_items = clean_data(
    analytics,
    orders,
    order_items
)

logging.info("Cleaning completed")

# ==========================
# TRANSFORM
# ==========================
logging.info("Starting transformation stage")

indicators = transform_data(
    analytics,
    orders,
    order_items
)

logging.info("Transformation completed")

# ==========================
# LOAD
# ==========================
logging.info("Saving output file")

load_data(indicators)

logging.info("CSV saved")

# ==========================
# VISUALIZE
# ==========================
logging.info("Generating graphs")

create_graphs(indicators)

logging.info("Graphs created")

print("\nPipeline completed.")
logging.info("Pipeline finished.")