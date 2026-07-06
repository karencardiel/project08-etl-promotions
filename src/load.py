import logging

def load_data(indicators):

    logging.info("LOAD STAGE")

    indicators.to_csv(
        "data/promotion_analysis.csv",
        index=False
    )

    logging.info("CSV exported successfully.")

    print("CSV exported.")