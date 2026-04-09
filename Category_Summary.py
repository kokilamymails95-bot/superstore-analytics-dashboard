import pandas as pd

file_path = r"C:\Users\System 66\Downloads\data\superstore_cleaned_data76.xlsx"
df = pd.read_excel(file_path)

# Total Spend
cols = ['MntWines','MntFruits','MntMeatProducts',
        'MntFishProducts','MntSweetProducts','MntGoldProds']

# Convert to Category format
category = df.melt(['Year','Month'], cols, 'Category', 'Revenue')

# Group
category_summary = category.groupby(
    ['Year','Month','Category']
)['Revenue'].sum().reset_index()

# Revenue %
category_summary['RevenuePct'] = (
    category_summary['Revenue'] /
    category_summary.groupby(['Year','Month'])['Revenue'].transform('sum') * 100
)

# Cumulative %
category_summary['CumulativePct'] = category_summary.groupby(
    ['Year','Month']
)['RevenuePct'].cumsum()

# -------------------------------
# 8. EXPORT TO EXCEL
# -------------------------------

output_path = r"C:\Users\System 66\Downloads\data\superstore_cleaners19_pro.xlsx"

with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    df.to_excel(writer,
               sheet_name='Customer_Master',
               index=False)

    category_summary.to_excel(writer, sheet_name='Category_summary1', index=False)
