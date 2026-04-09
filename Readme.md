# Superstore Sales Analysis 

## Overview
This project analyzes **Superstore sales performance and customer trends** using Python for data preparation and **Power BI** for interactive dashboards.  
It highlights revenue patterns, churn risk, category contributions, and customer segmentation to support business decision-making.

## Dataset
- Source: [Kaggle - Superstore Dataset](https://www.kaggle.com/)  
- Contains transactional sales data including:
  - Customer demographics
  - Product categories (Wines, Meat, Gold, Fish, Fruits, Sweets)
  - Purchase channels (Store, Web, Catalog)
  - Revenue and churn indicators
- Cleaned and transformed version: `SuperStore_Cleaned_Data.xlsx`

## Key Insights
- **Total Customers:** 2.21K  
- **Total Revenue:** 1.33M  
- **Top 20% Customers contribute:** 52.54% of revenue  
- **Churn Rate:** 33.3%  
- **Average Spend per Customer:** 601  

### Revenue Trends
- **Top Revenue Year:** 2013  
- **Lowest Revenue Year:** 2014  
- **Peak Month:** August  
- **Quarterly Trend:** Revenue peaked in Q3 across years  

### Category Contribution
- Wines: 50% of revenue  
- Meat Products: 28%  
- Gold Products: 7%  
- Fish Products: 6%  
- Sweets & Fruits: 8% combined  

### Customer Segmentation
- **Age Group Spend:**  
  - 65+ are the highest spenders (~0.41M each)  
  - Younger (35–44) groups spend significantly less  
- **Channel Performance:**  
  - Store Purchases: 46.3%  
  - Web Purchases: 32.5%  
  - Catalog Purchases: 21.1%  

### Churn Risk Analysis
- Revenue decline observed in 2014 due to higher churn.  
- High-value customers show reduced frequency, indicating retention challenges.

## Workflow
1. **Data Cleaning** – Python scripts for preprocessing (`Data_Cleaning.py`)  
2. **Exploratory Analysis** – Category, channel, and age-based segmentation  
3. **Churn Risk Analysis** – Identifying high-risk customers  
4. **Dashboard** – Power BI `.pbix` file for interactive visualization  
