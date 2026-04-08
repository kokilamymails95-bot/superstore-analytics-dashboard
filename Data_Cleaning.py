# Remove duplicates
df = df.drop_duplicates()
# Handle missing income
df['Income'] = df['Income'].fillna(df['Income'].median())
# Convert date column
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%m/%d/%Y').dt.strftime('%d-%m-%Y')
# Create Age
current_year = datetime.now().year
df['Age'] = current_year - df['Year_Birth']
# Remove unrealistic values
df = df[(df['Age'] >= 18) & (df['Age'] <= 80)]
df = df[df['Income'] > 0]
output_path = r"C:\Users\System 66\Downloads\data\SuperStore_Cleaned_Data74.xlsx"
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
   df.to_excel(writer,
               sheet_name='Customer_Master',
               index=False)
   summary.to_excel(writer, sheet_name='summary_Data1', index=False)
