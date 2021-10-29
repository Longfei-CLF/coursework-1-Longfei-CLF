# Write code that prepares your data
import pandas as pd

df = pd.read_excel('GVP_Eruption_Results.xls', 'EruptionList')
df = pd.read_excel(r'data.xlsx',sheetname=0)