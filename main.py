import pandas as pd 
import numpy as np 

# Read data into a dataframe
data = pd.read_csv('nyc_benchmarking_disclosure_data_reported_in_2017.csv')

# Replace all occurrences of Not Available with numpy not a number
data = data.replace({'Not Available': np.nan})

# Iterate through the columns
for col in list(data.columns):
    # Select columns that should be numeric
    if ('ft²' in col or 'kBtu' in col or 'Metric Tons CO2e' in col or 'kWh' in 
        col or 'therms' in col or 'gal' in col or 'Score' in col):
        # Convert the data type to float
        data[col] = data[col].astype(float)

# Display top of dataframe
print(data.info())