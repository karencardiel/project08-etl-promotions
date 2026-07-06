import pandas as pd
import logging

def transform_data(analytics, orders, order_items):

    logging.info("TRANSFORM STAGE")

    # =========================
    # BASIC METRICS
    # =========================
    total_sessions = analytics["session_id"].nunique()
    total_promo_clicks = analytics["promo_clicks_count"].sum()
    total_cart_after_promo = analytics["cart_after_promo_count"].sum()
    total_add_to_cart = analytics["clicks_add_to_cart"].sum()

    # =========================
    # BEHAVIOR METRICS
    # =========================

    # Sessions with at least 1 promo click
    sessions_with_promo = analytics[
        analytics["promo_clicks_count"] > 0
    ]["session_id"].nunique()

    # Sessions that added to cart after promo
    sessions_cart_after_promo = analytics[
        analytics["cart_after_promo_count"] > 0
    ]["session_id"].nunique()

    # Conversion rate: promo → cart
    if sessions_with_promo > 0:
        conversion_rate = sessions_cart_after_promo / sessions_with_promo
    else:
        conversion_rate = 0

    # =========================
    # CREATE FINAL TABLE
    # =========================

    indicators = pd.DataFrame({
        "Metric": [
            "Total Sessions",
            "Total Promo Clicks",
            "Sessions with Promo",
            "Sessions Cart After Promo",
            "Total Add to Cart Clicks",
            "Conversion Rate (Promo → Cart)"
        ],
        "Value": [
            total_sessions,
            total_promo_clicks,
            sessions_with_promo,
            sessions_cart_after_promo,
            total_add_to_cart,
            round(conversion_rate, 3)
        ]
    })

    logging.info("Indicators calculated successfully")

    print("\nFINAL INDICATORS")
    print(indicators)

    return indicators