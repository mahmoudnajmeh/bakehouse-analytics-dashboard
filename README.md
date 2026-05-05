# 🥐 Bakehouse Analytics Dashboard

A complete data analytics project built on **Databricks** using Delta Live Tables (DLT) pipelines and AI/BI Dashboards. This project analyzes sales performance, product demand, and customer sentiment for a bakery chain.

---

## Author
**Mahmoud Najmeh**  
<img src="https://avatars.githubusercontent.com/u/78208459?u=c3f9c7d6b49fc9726c5ea8bce260656bcb9654b3&v=4" width="200px" style="border-radius: 50%;">

------------------------------------------------------------------------

## 📊 Project Overview

This project demonstrates a complete production-grade analytics workflow on Databricks Free Edition:

1. **Data Ingestion** – CSV files uploaded to Databricks tables
2. **DLT Pipeline** – Automated ETL with Bronze, Silver, Gold layers
3. **Data Quality** – Expectations to validate data integrity
4. **Sentiment Analysis** – Customer reviews classified using rule-based logic
5. **Dashboard Creation** – Interactive AI/BI dashboard with three key visualizations

---

## 📈 Visualizations

The dashboard contains three main components:

### 1. Best Selling Products (Bar Chart)
- **Purpose:** Identify which products drive the most sales volume
- **Key Insight:** Croissant is the best-selling product (58 units), followed by Coffee (47 units) and Baguette (13 units)
- **Source Table:** `gold_product_sales`

### 2. Store Performance by City (Table)
- **Purpose:** Compare revenue and transaction volume across different cities
- **Key Insight:** New York generates the highest revenue ($158.50), followed by Los Angeles ($144.50)
- **Source Table:** `gold_city_performance`

### 3. Customer Sentiment Breakdown (Pie Chart)
- **Purpose:** Understand customer satisfaction based on review ratings
- **Key Insight:** 50% Positive, 20% Neutral, 30% Negative
- **Source Table:** `silver_reviews`

---

## 🏗️ Pipeline Architecture (Delta Live Tables)

The project includes a production-grade DLT pipeline that automates the entire ETL process:

### Bronze Layer (Raw Data)
| Table | Source | Description |
|-------|--------|-------------|
| `bronze_sales` | superstore_sales.csv | Raw sales data with schema inference |
| `bronze_reviews` | customer_reviews.csv | Raw customer reviews |

### Silver Layer (Cleaned Data)
| Table | Source | Transformations |
|-------|--------|-----------------|
| `silver_sales` | bronze_sales | Data validation with expectations |
| `silver_reviews` | bronze_reviews | Sentiment classification based on rating |

### Gold Layer (Aggregated Data)
| Table | Source | Purpose |
|-------|--------|---------|
| `gold_product_sales` | silver_sales | Best selling products by units and revenue |
| `gold_city_performance` | silver_sales | Store performance metrics by city |

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Databricks Community Edition** | Free cloud platform for data analytics |
| **Delta Live Tables (DLT)** | Declarative ETL pipeline framework |
| **Databricks SQL** | Querying and aggregating data |
| **AI/BI Dashboards** | Creating interactive visualizations |
| **GitHub** | Portfolio hosting and version control |

---

## 📁 Dataset Schema

### `superstore_sales` (20 rows)

| Column | Type | Description |
|--------|------|-------------|
| `order_id` | INT | Unique transaction ID |
| `order_date` | DATE | Date of purchase |
| `customer_name` | STRING | Customer identifier |
| `product_name` | STRING | Product sold (Croissant, Coffee, Baguette) |
| `product_category` | STRING | Bakery or Beverage |
| `quantity` | INT | Number of units sold |
| `price` | FLOAT | Price per unit |
| `revenue` | FLOAT | Total revenue |
| `city` | STRING | New York, Los Angeles, Chicago, Miami |
| `region` | STRING | East or West |

### `customer_reviews` (10 rows)

| Column | Type | Description |
|--------|------|-------------|
| `review_id` | INT | Unique review ID |
| `customer_name` | STRING | Customer identifier |
| `review_text` | STRING | Raw text review |
| `rating` | INT | Numeric rating (1–5) |

---

## 🔬 DLT Pipeline

The full pipeline code is available in the repository:
- [`bakehouse_dlt_pipeline.py`](bakehouse_dlt_pipeline.py)

The pipeline implements:
- Bronze layer: Raw CSV ingestion
- Silver layer: Data validation with expectations
- Gold layer: Aggregations for the dashboard

---

## 🖼️ Screenshots

### 1. Dashboard Visualizations

#### Best Selling Products (Bar Chart)

![Best Selling Products](https://github.com/user-attachments/assets/4ded9515-f000-4d7e-841a-02cd755ceed0)

#### Store Performance by City (Table)

![Store Performance](https://github.com/user-attachments/assets/1fee0a72-7436-4771-8afd-ce45f72859de)

#### Customer Sentiment (Pie Chart)

![Customer Sentiment](https://github.com/user-attachments/assets/bf0e392a-43be-46bb-b690-219eff3f6af3)

---

### 2. DLT Pipeline Graph

![DLT Pipeline](https://github.com/user-attachments/assets/09784dd5-517a-4ea5-9432-b2e6fe059294)

---

### 3. Gold Tables (Query Results)

#### `gold_product_sales`

![Gold Product Sales](https://github.com/user-attachments/assets/4c3f9dee-af86-43d5-8f14-b2463c09847d)

#### `gold_city_performance`

![Gold City Performance](https://github.com/user-attachments/assets/4b7e7306-3c31-40f2-901f-6962b87e5259)

#### `silver_reviews`
*Cleaned reviews with sentiment labels (Positive/Neutral/Negative).*

![Silver Reviews](https://github.com/user-attachments/assets/aa3c6c7e-b528-4d70-b9a4-683abd61a443)
