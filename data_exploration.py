# Write code that explores your data set
# Start to use pandas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data set
cleaned_file = "Cleaned_GVP_Eruption_Results.xlsx"
df = pd.read_excel(cleaned_file)

# Check the dtype of the prepared data
print(df.dtypes)




