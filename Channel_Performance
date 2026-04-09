import pandas as pd
file_path = r"C:\Users\System 66\Downloads\data\superstore_cleaned_data76.xlsx"
df = pd.read_excel(file_path)

# Total Spend
cols = ['NumDealsPurchases','NumWebPurchases','NumCatalogPurchases','NumStorePurchases']

# Convert to Category format
purchase = df.melt(['Year','Month'], cols, 'Purchase_Source', 'Value')

# Group
purchase_summary = purchase.groupby(
   ['Year','Month','Purchase_Source']
)['Value'].sum().reset_index()

# -------------------------------
# 8. EXPORT TO EXCEL
# -------------------------------

output_path = r"C:\Users\System 66\Downloads\data\superstore_cleaned_Data.xlsx"
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
   df.to_excel(writer,
              sheet_name='Customer_Master',
              index=False)
   purchase_summary.to_excel(writer, sheet_name='purchase_summary', index=False)


