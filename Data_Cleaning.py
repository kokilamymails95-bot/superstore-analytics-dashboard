# Import Libraries
import pandas as pd
from datetime import datetime

# Remove duplicates
df = df.drop_duplicates()
# Handle missing income
df['Income'] = df['Income'].fillna(df['Income'].median())

# Convert date column
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%m/%d/%Y')

#Segment Date & Year
df['Year'] = df['Dt_Customer'].dt.year
df['Month'] = df['Dt_Customer'].dt.month
df['Quarter'] = df['Dt_Customer'].dt.quarter

# Create Age
current_year = datetime.now().year
df['Age'] = current_year - df['Year_Birth']

# Remove unrealistic values
df = df[(df['Age'] >= 18) & (df['Age'] <= 80)]
df = df[df['Income'] > 0]
# Flags & segments
df['HasKids'] = ((df['Kidhome'] + df['Teenhome']) > 0).astype(int)
df['AgeBand'] = pd.cut(df['Age'],
    bins=[18,35,45,55,65,80],
    labels=['18-34','35-44','45-54','55-64','65+']
)
#Calculate Total Spend
SPEND_COLS = ['MntWines','MntFruits','MntMeatProducts',
              'MntFishProducts','MntSweetProducts','MntGoldProds']
df['TotalSpend']     = df[SPEND_COLS].sum(axis=1)
df['SpendTier'] = pd.qcut(df['TotalSpend'], 3, labels=['Low','Mid','High'])
df['IncomeTier'] = pd.qcut(df['Income'], 3, labels=['Low','Mid','High'])
output_path = r"C:\Users\System 66\Downloads\data\SuperStore_Cleaned_Data.xlsx"
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
   df.to_excel(writer,
               sheet_name='Customer_Master',
               index=False)
  
