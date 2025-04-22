import pandas as pd
from sqlalchemy import create_engine

data = pd.read_csv('files/sales_orders_1000.csv')
print (data)
# print(data.isnull().sum())
city_region_map = {
    'Karachi': 'South',
    'Lahore': 'North',
    'Islamabad': 'North',
    'Peshawar': 'North',
    'Quetta': 'South',
    'Multan': 'South',
    # Add more cities if needed
}

def tranfrom(data):
    data['Total_Price'] = data['Price']* data['Quantity']
    # convert orderdate to date time format
    data['OrderDate'] = pd.to_datetime(data['OrderDate'])
    # extract month
    data['Month'] = data['OrderDate'].dt.month_name()
    # convert city into region
    data['Region'] = data['City'].map(city_region_map)
    city_index = data.columns.get_loc('City')
    columns = list(data.columns)
    columns.remove('Region')
    columns.insert(city_index +1 , 'Region')
    data = data[columns]
    # data.to_csv('updateOrder.csv' ,index=False /)
tranfrom(data)

def load():
    try:
       data = pd.read_csv('files/sales_orders_1000.csv')
       engine = create_engine('mysql+pymysql://root:123456@localhost/ordersdb')
       data.to_sql('orders', con=engine, if_exists='replace', index=False)
       print("✅ Data loaded to MySQL database successfully!")
    except Exception as e:
        print(e)
load()