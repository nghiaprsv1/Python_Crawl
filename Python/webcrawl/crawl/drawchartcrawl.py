import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import json
import pandas as pd
import requests
import time
import random
import sqlite3
from tqdm import tqdm
def drawchart():
    datas = pd.read_csv("datathoitrang.csv")
    datas.drop(['short_url','image'],axis=1, inplace=True)
    data_brand= datas['brand_name'].value_counts().to_frame()
    data_brand.reset_index(inplace=True)
    data_brand.columns = ['brand_name','count']
    plt.figure(figsize=(13,10))
    sns.barplot(x='brand_name', y="count",data = data_brand)
    plt.xlabel("Thương hiệu")
    plt.ylabel("Số lượng")
    plt.title("Số lượng sản phẩm đến từ thương hiệu")
    plt.xticks(rotation= 90)
    plt.plot()
    plt.savefig('C://Users//nghia//Python_Crawl//Python//webcrawl//crawl//static//app//images//dothibrand.png')

    data_name_shop= datas['current_seller'].value_counts().to_frame()
    data_name_shop.reset_index(inplace=True)
    plt.figure(figsize=(14,28))
    sns.barplot(x='current_seller', y="count",data = data_name_shop)
    plt.xlabel("Tên cửa hàng")
    plt.ylabel("Giá trị")
    plt.title("Biểu đồ số lượng sản phẩm của cửa hàng")
    plt.xticks(rotation= 90)
    plt.plot()
    plt.savefig('C://Users//nghia//Python_Crawl//Python//webcrawl//crawl//static//app//images//dothishop.png')

    datas = pd.read_csv("datathoitrang.csv")
    quantity_value = datas.groupby('brand_name').sum()['quantity_sold']
    quantity_value.min()
    quantity_value.reset_index(inplace=False)
    quantity_value = quantity_value.reset_index().rename(columns={'quantity_sold': 'brand_name', 'brand_name': 'quantity_sold'})
    quantity_value.head()
    plt.figure(figsize=(13,10))
    sns.barplot (x='quantity_sold', y="brand_name",data = quantity_value)
    plt.xlabel("Brand Name")
    plt.ylabel("quantity_sold")
    plt.title("Số lượng sản phẩm đã bán của mỗi thương hiệu")
    plt.xticks(rotation= 90)
    plt.plot()
    plt.savefig('C://Users//nghia//Python_Crawl//Python//webcrawl//crawl//static//app//images//dothibrandsold.png')

    data3 = pd.read_csv("datathoitrang.csv")
    quantity_value = data3.groupby('current_seller').sum()['quantity_sold']
    quantity_value.reset_index(inplace=False)
    quantity_value = quantity_value.reset_index().rename(columns={'quantity_sold': 'current_seller', 'current_seller': 'quantity_sold'})
    quantity_value.head()
    plt.figure(figsize=(15,10))
    sns.barplot (x='quantity_sold', y='current_seller',data = quantity_value)
    plt.xlabel("Tên Cửa Hàng")
    plt.ylabel("quantity_sold")
    plt.title("Số lượng sản phẩm đã bán của mỗi cửa hàng")
    plt.xticks(rotation= 90)
    plt.plot()
    plt.savefig('C://Users//nghia//Python_Crawl//Python//webcrawl//crawl//static//app//images//dothishopsold.png')