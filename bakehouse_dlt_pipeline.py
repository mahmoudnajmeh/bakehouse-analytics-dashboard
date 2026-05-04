import dlt
from pyspark.sql.functions import *

@dlt.table(
    name="silver_sales",
    comment="Cleaned and validated sales data"
)
def silver_sales():
    return (
        spark.read.table("workspace.default.superstore_sales")
        .withColumn("ingestion_timestamp", current_timestamp())
    )

@dlt.table(
    name="silver_reviews",
    comment="Cleaned customer reviews with sentiment"
)
def silver_reviews():
    return (
        spark.read.table("workspace.default.customer_reviews")
        .select(
            "review_id",
            "customer_name",
            "review_text",
            "rating"
        )
        .withColumn(
            "sentiment",
            when(col("rating") >= 4, "Positive")
            .when(col("rating") == 3, "Neutral")
            .otherwise("Negative")
        )
        .withColumn("ingestion_timestamp", current_timestamp())
    )

@dlt.table(
    name="gold_product_sales",
    comment="Aggregated product sales for dashboard"
)
def gold_product_sales():
    return (
        spark.read.table("silver_sales")
        .groupBy("product_name")
        .agg(
            sum("quantity").alias("total_units_sold"),
            sum("revenue").alias("total_revenue"),
            count("order_id").alias("number_of_orders")
        )
        .orderBy(col("total_units_sold").desc())
    )

@dlt.table(
    name="gold_city_performance",
    comment="City performance metrics for dashboard"
)
def gold_city_performance():
    return (
        spark.read.table("silver_sales")
        .groupBy("city")
        .agg(
            countDistinct("order_id").alias("total_orders"),
            sum("quantity").alias("items_sold"),
            sum("revenue").alias("total_revenue"),
            round(avg("revenue"), 2).alias("avg_order_value")
        )
        .orderBy(col("total_revenue").desc())
    )

@dlt.table(
    name="gold_sentiment_summary",
    comment="Sentiment summary for dashboard"
)
def gold_sentiment_summary():
    return (
        spark.read.table("silver_reviews")
        .groupBy("sentiment")
        .agg(
            count("review_id").alias("review_count")
        )
    )