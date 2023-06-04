import requests
import json
import pandas as pd
import numpy as np
import sqlalchemy
import pypyodbc as odbc

url = "https://api.metalpriceapi.com/v1/latest?api_key=3693bf8d4dc56dddf351f695ed69fcf1&base=USD&currencies=INR,EUR,XAU,XAG"
access_key = "3693bf8d4dc56dddf351f695ed69fcf1"
response = requests.get(url)
resp = json.loads(response.text)
print(resp)
timestamp = resp['timestamp']
base = resp['base']
rate = resp['rates']
inr = rate['INR']
eur = rate['EUR']
today_trade = np.array([timestamp,base,inr,eur])
data_frame = pd.DataFrame(today_trade)
print(data_frame)
print(today_trade)
