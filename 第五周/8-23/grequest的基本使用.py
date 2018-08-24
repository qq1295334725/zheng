"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:grequest的基本使用.PY
@ide:PyCharm
@time:2018-08-23 10:17:56
"""
import grequests
import requests

import time
# grequests是基于requests库实现的一个异步请求库，它支持requests库中各种用法，由于它结合了requests和gevent库（实现协程的一个库），所以他的请求效率非常高
urls = ["http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get","http://httpbin.org/get"]

def use_requests():
    t1 = time.time()
    print("开始执行时间：",t1)
    for url in urls:
        res = requests.get(url)
        # print(res)
    t2 = time.time()
    print("结束时间：",t2)
    t3 = t2 - t1
    print("总耗时：",t3)
#
def use_grquests():
    t1 = time.time()
    print("开始执行时间：", t1)
    tasks = (grequests.get(url) for url in urls)
    # 所有网址对应的response对象列表
    # size表示同时访问的网址数
    res = grequests.imap(tasks,size=20)
    # 遍历response列表，取出每一个response对象
    for r in res:
        print(r)
    t2 = time.time()
    print("结束时间：", t2)
    t3 = t2 - t1
    print("总耗时：", t3)

# use_requests()
use_grquests()
















