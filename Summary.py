
# -------------------------------
# 1. IMPORT LIBRARIES
# -------------------------------
import pandas as pd
import numpy as np
from datetime import datetime
from scipy.stats import chi2_contingency
# -------------------------------
# 2. LOAD DATA
# -------------------------------
file_path = r"C:\Users\System 66\Downloads\data\SuperStore_Cleaned_Data76.xlsx"
df = pd.read_excel(file_path)
summary = pd.DataFrame()
# Cleaner pandas way — same result as using +
cols = ['MntWines', 'MntFruits', 'MntMeatProducts',
      'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
df['TotalSpend'] = df[cols].sum(axis=1)

def churn_risk_from_recency(r):
    if r <= 33:
        return 'Low'
    elif r <= 66:
        return 'Medium'
    else:
        return 'High'

df['ChurnRisk'] = df['Recency'].apply(churn_risk_from_recency)
# Churn% — High risk customers / total customers
churn_pct = round((df['ChurnRisk'] == 'High').sum() / len(df) * 100, 2)

# Add to summary
summary['Total Revenue'] = [df['TotalSpend'].sum()]
summary['Total Customers'] = [df['Id'].nunique()]
summary['Avg Spend'] = [round(df['TotalSpend'].mean(), 2)]
summary['Top 20% Revenue (%)'] = [round(
  df.groupby('Id')['TotalSpend'].sum().pipe(
      lambda x: x.nlargest(int(0.2 * len(x))).sum() / x.sum() * 100
  ), 2)]

# Flags & segments
df['HasKids'] = ((df['Kidhome'] + df['Teenhome']) > 0).astype(int)
df['AgeBand'] = pd.cut(df['Age'],
    bins=[18,35,45,55,65,80],
    labels=['18-34','35-44','45-54','55-64','65+']
)
df['SpendTier'] = pd.qcut(df['TotalSpend'], 3, labels=['Low','Mid','High'])
df['IncomeTier'] = pd.qcut(df['Income'], 3, labels=['Low','Mid','High'])

summary['Churn Rate (%)'] = [churn_pct]
output_path = r"C:\Users\System 66\Downloads\data\marketing_analysis_output.xlsx"
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
   df.to_excel(writer,sheet_name='Customer_Master',index=False)
   summary.to_excel(writer, sheet_name='summary_Data1', index=False)

