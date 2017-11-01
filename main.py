'''Wweb page tester by dscdtc'''
#usr/bin/python3
import requests
import pandas as pd
from threading import Thread

def get_status(url):
    try:
        r = requests.get(url, timeout=2, allow_redirects=False)
        return r.status_code
    except requests.exceptions.ConnectTimeout:
        return 'timeout!'

result = []
class TestThread(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url
    def run(self):
        result.append(get_status(self.url))
    # def get_result(self):
    #     return self.result

df = pd.read_csv('./api_list_demo.csv', usecols=[0,1], encoding='utf-8')
#for index, url in enumerate(df.iloc[:, 1]):
for url in df.iloc[:, 1]:
    thd = TestThread(url)
    thd.start()
thd.join()
print(result)
df['状态码'] = result
df.to_csv('./result/result.csv',encoding='utf-8', index=False)

print("Test finish!")
