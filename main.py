'''Tester for web page test'''
#usr/bin/python3
import requests
import pandas as pd
import json

def get_status(url):
    r = requests.get(url, allow_redirects=False)  
    return r.status_code

result = []
df = pd.read_csv('./api_list.csv', usecols=[0,1], encoding='utf-8')
for url in df.iloc[:, 1]:
    result.append(get_status(url))
df['状态码'] = result

df.to_csv('./result/result.csv',encoding='utf-8', index=False)
