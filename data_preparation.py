# Start to use pandas
import pandas as pd
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
new_orgianl_file = "New_GVP_Eruption_Results.xls"

df=pd.read_excel(new_orgianl_file, sheet_name='Eruption List', skiprows=1)

print(df.columns)
print(df.shape)

