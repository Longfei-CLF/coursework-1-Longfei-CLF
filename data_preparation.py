# Write code that prepares your data
import pandas as pd
orgianl_file = "GVP_Eruption_Results.xls"
df = pd.read_excel(orgianl_file, sheet_name='Eruption List')