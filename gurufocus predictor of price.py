#!/usr/bin/env python
# coding: utf-8

# Note that this code assumes that you have already obtained an API key from GuruFocus and that you have installed the necessary Python libraries (requests, pandas, numpy, seaborn, and matplotlib) in your environment.

# In[1]:


#This code will loop through the list of required libraries and try to import each one using the importlib module. 
#If a library is successfully imported, it will print a message saying that the library was found. 
#If a library is not found, it will print a message saying that the library was not found.

#You should run this code snippet before running the previous code to make sure that all the necessary libraries are installed in your environment.



import importlib

# List of required libraries
libraries = ['requests', 'pandas', 'numpy', 'seaborn', 'matplotlib']

# Check if each library is installed and print the results
for lib in libraries:
    try:
        importlib.import_module(lib)
        print(f'{lib} library found!')
    except ImportError:
        print(f'{lib} library not found!')


# In[ ]:


import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Enter your API key here
api_key = 'your_api_key'

# Set the stock symbol you want to analyze
symbol = 'AAPL'

# Define the API endpoint
url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={api_key}'

# Call the API to get the stock's historical price data
response = requests.get(url)
data = response.json()

# Parse the JSON response into a Pandas DataFrame
df = pd.DataFrame(data['historical'])

# Calculate the daily price change
df['price_change'] = df['close'].diff()

# Calculate the daily percent change
df['percent_change'] = df['close'].pct_change()

# Calculate the rolling 30-day correlation coefficient for all variables
corr_matrix = df.rolling(window=30).corr()

# Get the correlation coefficients for each variable with the price change
price_change_correlations = corr_matrix.loc['price_change', :].drop('price_change')

# Get the variable with the highest correlation coefficient
best_variable = price_change_correlations.abs().idxmax()

# Plot the correlation matrix heatmap
sns.heatmap(corr_matrix.loc['price_change', :], cmap='coolwarm')
plt.title(f'30-Day Correlation Matrix ({symbol})')
plt.show()

# Print the results
print(f'The variable with the highest correlation coefficient with price change is {best_variable}.')

