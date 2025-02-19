# Perform Various operations on Data Cube Technology 2.Multidimensional Data analysis

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data_cube=pd.read_csv('data_cube.csv',index_col=['Region','Product'])

#Visualization
product_sales=data_cube.groupby('Product').sum()
product_sales.plot(kind='bar',stacked=True,figsize=(10,6))
plt.title('Total Sales by Product across Regions')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

region_sales=data_cube.groupby('Region').sum()
region_sales.plot(kind='bar',stacked=True,figsize=(10,6))
plt.title('Total Sales by Region across Months')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()

month_sales=data_cube.sum(axis=0)
month_sales.plot(kind='bar',stacked=True,figsize=(10,6))
plt.title('Total Sales by Month across Products')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()
