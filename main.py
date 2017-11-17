#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''Web page tester by dscdtc'''

from datetime import datetime
from threading import Thread
import pandas as pd
import requests
import os

from public import screenshot

RESULT = list()
FILENAME = datetime.now().strftime('%y-%m-%d %H:%M')
os.mkdir('./result/img/'+FILENAME)

class TestThread(Thread):
    'Creat Multi-thread'
    def __init__(self, url, name):
        Thread.__init__(self)
        self.url = url
        self.pic = './result/img/%s/%s.png' % (FILENAME, name)
    # @staticmethod
    def get_status(self):
        'Get webpage status code'
        try:
            res = requests.get(self.url, timeout=3, allow_redirects=False)
            return res.status_code if res else 'No Response'
        except requests.exceptions.ConnectTimeout:
            return 'Timeout!'
    def run(self):
        RESULT.append(self.get_status())
        screenshot.take_screenshot(self.url, self.pic)

DF = pd.read_csv('./api_list_demo.csv', usecols=[0, 1], encoding='utf-8')
NAME = DF.iloc[:, 0]

for index, url in enumerate(DF.iloc[:, 1]):
    thd = TestThread(url, NAME[index])
    thd.setDaemon(True)
    thd.start()
    thd.join()

DF[u'状态码'] = RESULT

DF.to_csv('./result/csv/%s.csv' % FILENAME, encoding='utf-8', index=False)
print("Test finish!")
