import matplotlib.pyplot as plt
import logging

# Colores
PURPLE = "#521484"
ORANGE = "#daa031"

def create_graphs(indicators):

    logging.info("Generating clean professional graphs")

    # =========================
    # GRAPH 1: INDICATORS OVERVIEW
    # =========================
    plt.figure(figsize=(7,5))

    colors = [PURPLE, ORANGE, PURPLE, ORANGE, PURPLE, ORANGE]

    plt.bar(
        indicators["Metric"],
        indicators["Value"],
        color=colors
    )

    plt.xticks(rotation=45, ha="right", color="black")
    plt.yticks(color="black")

    plt.title("ETL Indicators - Promotion Impact Analysis", color="black")
    plt.ylabel("Value", color="black")

    plt.tight_layout()
    plt.savefig("graphs/indicators_bar.png", dpi=300)
    plt.close()

    # =========================
    # GRAPH 2: PROMO vs CART
    # =========================
    promo = float(indicators.loc[1, "Value"])
    cart = float(indicators.loc[3, "Value"])

    plt.figure(figsize=(6,4))

    plt.bar(
        ["Promo Clicks", "Cart After Promo"],
        [promo, cart],
        color=[ORANGE, PURPLE]
    )

    plt.xticks(color="black")
    plt.yticks(color="black")

    plt.title("Promotion vs Cart Behavior", color="black")
    plt.ylabel("Count", color="black")

    plt.tight_layout()
    plt.savefig("graphs/promo_vs_cart.png", dpi=300)
    plt.close()

    # =========================
    # GRAPH 3: PIPELINE INDICATORS
    # =========================
    plt.figure(figsize=(10,5))

    bars = plt.barh(
        indicators["Metric"],
        indicators["Value"],
        color=[PURPLE, ORANGE, PURPLE, ORANGE, PURPLE, ORANGE]
    )

    for bar in bars:
        width = bar.get_width()

        plt.text(
            width + max(indicators["Value"]) * 0.02,
            bar.get_y() + bar.get_height()/2,
            f"{width:.2f}",
            va="center",
            color="black"
        )

    plt.title("Pipeline Indicators", color="black")
    plt.xlabel("Value")
    plt.ylabel("Indicator")

    plt.grid(axis="x", alpha=0.3)

    plt.tight_layout()

    plt.savefig("graphs/pipeline_indicators.png", dpi=300)

    plt.close()

    # =========================
    # GRAPH 4: CONVERSION RATE
    # =========================
    rate = float(indicators.loc[5, "Value"])

    plt.figure(figsize=(7,5))

    plt.pie(
        [rate, 1 - rate],
        labels=["Converted", "Not Converted"],
        colors=[PURPLE, ORANGE],
        autopct="%1.1f%%",
        textprops={'color': "black"},
        startangle=90
    )

    plt.title("Promotion → Cart Conversion Rate", color="black")

    plt.savefig("graphs/conversion_rate.png", dpi=300)
    plt.close()

    logging.info("Clean graphs generated")
    print("Graphs updated.")