# 📊 End-to-End E-Commerce Data Pipeline & RFM Customer Segmentation

## 💡 Project Overview
This project delivers a production-grade, end-to-end **Data Analytics and Engineering Pipeline** using a real-world Brazilian E-Commerce dataset (Olist) containing over 100k orders. 

Instead of jumping straight into visualization, this project demonstrates a mature, **decoupled architecture (前后端分离)**: executing raw data extraction and engineering via high-performance SQL, performing advanced mathematical customer scoring with Python, and finally delivering executive-level business insights through an interactive Tableau Dashboard.

## 🛠️ Tech Stack & Role Breakdown

### 🔧 1. Data Engineering Layer (SQL / DuckDB)
*   **File:** `step1_extract.py`
*   **Role:** Implemented an in-memory database utilizing **DuckDB** to extract transactional records. Designed complex multi-table `JOIN` operations, handled missing values, and filtered out invalid order statuses (`canceled` / `unavailable`) to ensure data integrity.

### 🧠 2. Analytics & Modeling Layer (Python / Pandas)
*   **File:** `step2_transform.py`
*   **Role:** Built an automated **RFM (Recency, Frequency, Monetary)** customer value model. Resolved severe data skewness (95%+ single-time buyers) by implementing custom ranking and boundary distribution logic (`rank(method='first')` inside `pd.qcut`). Automatically segments the user base into **Champions**, **Potential Loyalists**, and **At Risk** tiers.

### 🎨 3. Business Intelligence Layer (Tableau Dashboard)
*   **Role:** Created a high-fidelity executive dashboard connected to the clean data pipeline. Features include interactive KPI scorecards, a cohort health donut breakdown, a revenue contribution bar chart (proving the 80/20 rule), and a sophisticated 5x5 R-M Matrix Heatmap for targeted marketing automation.
