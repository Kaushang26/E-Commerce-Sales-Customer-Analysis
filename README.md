# E‑Commerce Data Cleaning & Analysis

## 📌 Overview
This project demonstrates an **end‑to‑end data pipeline** for an e‑commerce system:
- **Data Cleaning** with SQL scripts
- **Data Analysis** with SQL + Python
- **CSV Export** for reporting
- **Power BI Dashboard** for visualization

The workflow connects a MySQL database to Python scripts, automates cleaning and analysis, and produces insights ready for business intelligence.

---

## 📂 Project Structure
Project Directory/
│
├── 1data/                # Raw dataset (CSV)
├── 2sql/                 # SQL scripts
│   ├── 01_create_tables.sql
│   ├── 02_insert_data.sql
│   ├── 03_data_cleaning.sql
│   └── 04_analysis.sql
├── 3python_work/         # Python scripts
│   ├── run_cleaning.py
│   ├── run_analysis.py
│   └── utils.py
├── 4dashboard_BI/        # Power BI dashboard files (.pbix)
├── 5result/              # Screenshots / outputs
├── 6report/              # Documentation / reports
└── README.md

## 📊 Analysis Queries


1-->**Top Selling Products**

2-->**Revenue by Customer**

3-->**Monthly Revenue Trends**

4-->**Repeat Buyers**

5-->**Inactive Customers**

6-->**Average Order Value (AOV)**

7-->**Declining Sales by Product**

8-->**Payment Method Distribution**

Each query result is exported as a CSV into results/csv/.

## 📈 Dashboard

Import CSVs into Power BI.

Build visuals:

Bar chart → Top Products

Line chart → Monthly Revenue

Table → Repeat Buyers

KPI → Average Order Value

Pie chart → Payment Distribution

Save the dashboard in 4dashboard_BI/.

##  📷 Screenshots
Include screenshots of:

**MySQL login and table view**

**Cleaning script execution**

**Analysis script execution**

CSV outputs in results/csv/



##  🚀 Future Improvements
Automate pipeline with pipeline.py

Schedule daily refresh using Task Scheduler

Connect Power BI directly to MySQL for live dashboards

Add advanced metrics (Customer Lifetime Value, churn prediction)

#  👨‍💻 Author
**Kaushang Tripathi**  