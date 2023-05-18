import sqlite3
import pandas as pd

df=pd.read_csv('crawled_data_ncds.csv')

df.columns = df.columns.str.strip()

connection = sqlite3.connect('db.sqlite3')

df.to_sql('crawl_product',connection, if_exists='replace')

connection.close()