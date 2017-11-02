'''Web page tester by dscdtc'''
#usr/bin/python3
import requests
import pandas as pd
from threading import Thread


result = []
class TestThread(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    @staticmethod
    def get_status(url):
        try:
            r = requests.get(url, timeout=1, allow_redirects=False)
            # print(r)
            return r.status_code if r else 'No Response'
        except requests.exceptions.ConnectTimeout:
            return 'timeout!'
    def run(self):
        result.append(self.get_status(self.url))
    # def get_result(self):
    #     return self.result

df = pd.read_csv('./api_list_demo.csv', usecols=[0,1], encoding='utf-8')
#for index, url in enumerate(df.iloc[:, 1]):
for url in df.iloc[:, 1]:
    thd = TestThread(url)
    # thd.setDaemon(True)
    thd.start()
    thd.join()

df['状态码'] = result

df.to_csv('./result/result.csv',encoding='utf-8', index=False)
print("Test finish!")
