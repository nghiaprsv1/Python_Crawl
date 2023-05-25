import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3

datas = pd.read_csv("crawled_data_ncds.csv")
num_rows = datas.shape[0]
print(num_rows)
datas.drop(['short_url','image'],axis=1, inplace=True)
data_brand= datas['brand_name'].value_counts().to_frame()
data_brand.reset_index(inplace=True)
data_brand.columns = ['brand_name','count']
print(data_brand)

plt.figure(figsize=(13,10))
sns.barplot(x='brand_name', y="count",data = data_brand)
plt.xlabel("Thương hiệu")
plt.ylabel("Số lượng")
plt.title("Số lượng sản phẩm đến từ thương hiệu")
plt.xticks(rotation= 90)
plt.plot()
plt.savefig('C://Users//nghia//Python_Crawl//Python//webcrawl//crawl//static//app//images//dothibrand.png')
datas = pd.read_csv("danhsachcuahangdaban.csv")
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