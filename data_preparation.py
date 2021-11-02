
#import pandas as pd
orgianl_file = "GVP_Eruption_Results.xls"
#df = pd.read_excel(orgianl_file, sheet_name='Eruption List', engine='xlrd')
# orgianl_file = "GVP.csv"
# df = pd.read_csv(orgianl_file, sep="", engine='python')

import pandas as pd
from bs4 import BeautifulSoup
import os

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



convert_to_xlsx()
df=pd.read_excel('Clean.xlsx', sheet_name='Eruption List', skiprows=1)

print(df.columns)
print(df.shape)

