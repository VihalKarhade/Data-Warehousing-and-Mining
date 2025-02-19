import pandas as pd
import numpy as np

df=pd.read_csv('sales_data.csv')
print(df)
df['Total_Sales']=df['Quantity']*df['Price']

data_cube=pd.pivot_table(df,values='Total_Sales',
                         index=['Region','Product'],
                         columns=['Month'],aggfunc='sum',
                         fill_value=0)
print("Data Cube:")
print(data_cube)

data_cube.to_csv('data_cube.csv')

data_cube=pd.read_csv('data_cube.csv')

data_cube.set_index(['Region','Product'],inplace=True)
print("\nLoaded Data Cube:")
print(data_cube)

#query 1
product_total_sales=data_cube.xs('Widget',level='Product').sum(axis=1)
print("\nTotal sales for 'Widget' across all regions and months:")
print(product_total_sales)

#Query 2
region_total_sales=data_cube.xs('North',level='Region').sum(axis=1)
print("\nTotal sales in 'North' region across all products and months:")
print(region_total_sales)

#Query 3
month_total_sales=data_cube.sum(axis=0).loc['January']
print("\nTotal Sales in 'January' across all regionsa and products:")
print(month_total_sales)
