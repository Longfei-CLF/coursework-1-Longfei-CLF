# Start to use pandas
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

orgianl_file = "GVP_Eruption_Results.xls"
## Outstanding issue in reading the file
# Orginal file downloaded from the website cannot be read by using df = pd.read_excel(orgianl_file, sheet_name='Eruption List')
# Error message: xlrd.biffh.XLRDError: Unsupported format, or corrupt file: Expected BOF record; found b'<?xml ve'
# I did some research and found the orginal file might be in xml format. Then I tried use beautifulsoup to convert the file into xlsx.
def convert_to_xlsx():
    with open(orgianl_file) as xml_file:
        soup = BeautifulSoup(xml_file.read(), 'xml')
        soup.prettify(formatter='html')
        str(soup)
        writer = pd.ExcelWriter('Clean.xlsx')
        for sheet in soup.findAll('Worksheet'):
            sheet_as_list = []
            for row in sheet.findAll('Row'):
                sheet_as_list.append([cell.Data.text if cell.Data else '' for cell in row.findAll('Cell')])
            pd.DataFrame(sheet_as_list).to_excel(writer, sheet_name=sheet.attrs['ss:Name'], index=False, header=False)

        writer.save()
# However, the converted xlsx file is incomplete.
# By following Sarah's suggestion, I opened the orginal file in excel and saved it as a new xlsx file called "New_GVP_Eruption_Results.xlsx"

## Beign the data prepartion with new orginal file.
new_orgianl_file = "New_GVP_Eruption_Results.xlsx"

# Load the data set from the file and skip the first row because it has a header
df = pd.read_excel(new_orgianl_file, sheet_name='Eruption List', skiprows=1)

# Print the columns name
print('Initial columns:')
print(df.columns)

# Rename final used columns
df.rename(columns={'Volcano Number':'Vol_num', 'Volcano Name':'Vol_name',
        'Start Year':'Sta_yr', 'Start Month':'Sta_mo', 'Start Day':'Sta_dy',
        'End Year':'End_yr', 'End Month':'End_mo', 'End Day':'End_dy',},
        inplace=True)
# Before dropping 'Eruption Category', obtain all confirmed eruptions
df = df[df['Eruption Category'] == 'Confirmed Eruption']
# Only obtain final used columns
final_cols = ['Vol_num', 'Vol_name', 'Sta_yr', 'Sta_mo', 'Sta_dy', 
    'End_yr', 'End_mo', 'End_dy', 'VEI']
df = df[final_cols]

# Delete data earlier than 1700 due to limit of dtype (datetime64[ns]), 585 years (2^64 nanoseconds).
df.drop(df[(df.Sta_yr <= 1700)].index, inplace=True)
# Replace all 0 into NaN
df.replace(0,np.nan,inplace=True)
# Check for missing values
print(df.isna().sum())
# Remove the rows contain missing values
df.dropna(axis=0, how='any', inplace=True)

#Convert dtype from object to int
df = df.convert_dtypes()
# Create the start date column and convert the data type from str into Datetime64
df['Sta_date'] = df.Sta_yr.astype(str) + ' ' + df.Sta_mo.astype(str) + ' ' + df.Sta_dy.astype(str)
df['Sta_date'] = pd.to_datetime(df['Sta_date'],format='%Y-%m-%d')
df['End_date'] = df.End_yr.astype(str) + ' ' + df.End_mo.astype(str) + ' ' + df.End_dy.astype(str)
df['End_date'] = pd.to_datetime(df['End_date'])
# Calculate the eruption duration
df['Erup_dur'] = (df.End_date - df.Sta_date).dt.days

# Check all columns and dtype are correct
print(df.info(verbose=True))

# Export the cleaned data as Excel file for exploration
df.to_excel(r'Cleaned_GVP_Eruption_Results.xlsx', index=False)
