import pandas as pd

users_information=pd.read_csv('users.txt')
orders_information=pd.read_csv('orders.txt')

unified_information=pd.merge(users_information, orders_information, on='user_id')

print(unified_information.groupby('gender')['price'].sum())

print(unified_information['price'].sum())

print(unified_information.groupby('name')['price'].sum().sort_values(ascending=False).head(3))