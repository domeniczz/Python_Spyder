# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 17:48:43 2021

@author: Domenic
"""

# f = open("data/account.db", encoding="UTF-8")
# f = f.readlines()

# for line in f:  # one loop, one line
#     line = line.strip().split()
#     # print(line)
#     height = int(line[3])
#     weight = int(line[4])
#     if height >= 170 and weight <= 50:
#         print(line)


# 连续请求网站10次
import time
import requests

def gettext(i,website):
    try:
        r=requests.get(website,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return i
    except:
        return "产生错误"

website="https://www.eslfast.com/eslread/"

start_time=time.time()

for i in range(10):
    print("\r",gettext(i+1,website),end="")
print("\n")

end_time=time.time()

print("time:","{:.4f}".format(end_time-start_time))
