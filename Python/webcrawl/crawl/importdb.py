import json
import pandas as pd
import requests
import time
import random
import sqlite3
from tqdm import tqdm

def import_data(file_path):
        df1=pd.read_csv(file_path)
        df1.columns = df1.columns.str.strip()
        connection = sqlite3.connect('db.sqlite3')
        df1.to_sql('crawl_product',connection, if_exists='replace')
        connection.close()
