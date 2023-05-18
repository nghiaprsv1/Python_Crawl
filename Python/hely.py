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
plt.savefig('C:\\Users\\nghia\\OneDrive\\Máy tính\\Python\\webcrawl\\crawl\\static\\app\\images\\dothibrand.png')

data_name_shop= datas['current_seller'].value_counts().to_frame()
data_name_shop.reset_index(inplace=True)
print(data_name_shop)
plt.figure(figsize=(14,28))
sns.barplot(x='current_seller', y="count",data = data_name_shop)
plt.xlabel("Tên cửa hàng")
plt.ylabel("Giá trị")
plt.title("Biểu đồ số lượng sản phẩm của cửa hàng")
plt.xticks(rotation= 90)
plt.savefig('C:\\Users\\nghia\\OneDrive\\Máy tính\\Python\\webcrawl\\crawl\\static\\app\\images\\dothishop.png')