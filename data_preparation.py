# Start to use pandas
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

# Outstanding issue in reading the file
# Orginal file downloaded from the website cannot be read by using df = pd.read_excel(orgianl_file, sheet_name='Eruption List')
# Error message: xlrd.biffh.XLRDError: Unsupported format, or corrupt file: Expected BOF record; found b'<?xml ve'
# I did some research and found the orginal file might be in xml format. Then I tried use beautifulsoup to convert the file into xlsx.


def convert_to_xlsx():
    orgianl_file = "GVP_Eruption_Results.xls"
    with open(orgianl_file) as xml_file:
        soup = BeautifulSoup(xml_file.read(), 'xml')
        soup.prettify(formatter='html')
        str(soup)
        writer = pd.ExcelWriter('Clean.xlsx')
        for sheet in soup.findAll('Worksheet'):
            sheet_as_list = []
            for row in sheet.findAll('Row'):
                sheet_as_list.append(
                    [cell.Data.text if cell.Data else '' for cell in row.findAll('Cell')])
            pd.DataFrame(sheet_as_list).to_excel(
                writer, sheet_name=sheet.attrs['ss:Name'], index=False, header=False)

        writer.save()
# However, the converted xlsx file is incomplete.
# By following Sarah's suggestion, I opened the orginal file in excel and saved it as a new xlsx file called "New_GVP_Eruption_Results.xlsx"

# Beign the data prepartion with new orginal file.


def prepare_data(df):
    """
    Prepare the original data
    param: df Dataframe the raw data
    return: The prepared data
    rtype: Dataframe
    """
    print(df.columns)
    df.rename(columns={
        'Volcano Name': 'Vol_name', 'Start Year': 'Sta_yr',
        'Start Month': 'Sta_mo', 'Start Day': 'Sta_dy', 'End Year': 'End_yr',
        'End Month': 'End_mo', 'End Day': 'End_dy', },
        inplace=True)
    df = df[df['Eruption Category'] == 'Confirmed Eruption']
    final_cols = [
        'Vol_name', 'Sta_yr', 'Sta_mo', 'Sta_dy',
        'End_yr', 'End_mo', 'End_dy', 'VEI']
    df = df[final_cols]

    # Delete data earlier than 1700 due to limit of dtype (datetime64[ns]), 585 years (2^64 nanoseconds).
    df.drop(df[(df.Sta_yr <= 1700)].index, inplace=True)

    df.replace(0, np.nan, inplace=True)
    print(df.isna().sum())
    df.dropna(axis=0, how='any', inplace=True)
    df = df.convert_dtypes()
    df['Sta_date'] = df.Sta_yr.astype(
        str) + ' ' + df.Sta_mo.astype(str) + ' ' + df.Sta_dy.astype(str)
    df['Sta_date'] = pd.to_datetime(df['Sta_date'], format='%Y-%m-%d')
    df['End_date'] = df.End_yr.astype(
        str) + ' ' + df.End_mo.astype(str) + ' ' + df.End_dy.astype(str)
    df['End_date'] = pd.to_datetime(df['End_date'])
    df['Erup_dur'] = (df.End_date - df.Sta_date).dt.days

    df_prepared = pd.DataFrame(
        df, columns=['Vol_name', 'Sta_yr', 'Erup_dur', 'VEI'])
    return df_prepared


if __name__ == '__main__':
    new_original_file = "New_GVP_Eruption_Results.xlsx"
    df_original = pd.read_excel(
        new_original_file, sheet_name='Eruption List', skiprows=1)
    df_prepared = prepare_data(df_original)

    print(df_prepared.info(verbose=True))
    print(df_prepared.head())

    df_prepared.to_excel('Cleaned_GVP_Eruption_Results.xlsx', index=False)
