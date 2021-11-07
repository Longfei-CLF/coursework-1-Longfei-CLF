
import pandas as pd
orgianl_file = "GVP_Eruption_Results.xls"
df = pd.read_excel(orgianl_file, sheet_name='Eruption List', engine='xlrd')
# orgianl_file = "GVP.csv"
# df = pd.read_csv(orgianl_file, sep="", engine='python')


