# ── 1. IMPORT LIBRARIES ─────────────────────────────
import pandas as pd
# ── 2. LOAD DATA ─────────────────────────────
file_path = r"C:\Users\System 66\Downloads\data\SuperStore_Cleaned_Data76.xlsx"
df = pd.read_excel(file_path)

# ── 3. CALCULATE TOTAL SPEND AND PURCHASES ─────────
SPEND_COLS = ['MntWines','MntFruits','MntMeatProducts',
              'MntFishProducts','MntSweetProducts','MntGoldProds']
PURCHASE_COLS = ['NumDealsPurchases','NumWebPurchases',
                 'NumCatalogPurchases','NumStorePurchases']

# Create summary dataframe
summary = pd.DataFrame()
summary['TotalSpend']     = df[SPEND_COLS].sum(axis=1)
summary['TotalPurchases'] = df[PURCHASE_COLS].sum(axis=1)
summary['AvgSpend']       = df[SPEND_COLS].mean(axis=1)
summary['MeanPurchases']  = df[PURCHASE_COLS].mean(axis=1)

# Copy Year and Month into summary
summary['Year'] = df['Year']
summary['Month'] = df['Month']
summary['Customers'] = df['Id'].shape[0]

# ── 4. CALCULATE CHURN RISK ────────────────────────
def churn_risk(recency):
    if recency <= 33:   return 'Low'
    elif recency <= 66: return 'Medium'
    else:               return 'High'

summary['ChurnRisk'] = df['Recency'].apply(churn_risk)

# ── 5. GROUP BY YEAR, MONTH, CHURNRISK ─────────────
Churn_risk = summary.groupby(['Year','Month','ChurnRisk']).agg(
    Customers=('TotalSpend','count'),   # Number of customers
    TotalSpend=('TotalSpend','sum'),
    TotalPurchases=('TotalPurchases','sum'),
    AvgSpend=('AvgSpend','mean'),
    MeanPurchases=('MeanPurchases','mean')
).round(2).reset_index()

# ── 6. EXPORT TO EXCEL ─────────────────────────────
output_path = r"C:\Users\System 66\Downloads\data\superstore_cleaned_pro.xlsx"
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    Churn_risk.to_excel(writer, sheet_name='Churn_Risk_Analysis', index=False)
