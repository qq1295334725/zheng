"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用随机请求头和代理IP爬取糗事百科.PY
@ide:PyCharm
@time:2018-08-08 09:26:51
"""
# 1.分析要爬取网站的URL，找到其中的规律
# 2.对网站发起请求，获取网页源代码
# 3.根据源代码，使用正则表达式匹配出来我们想要的信息。
# 4.把获取到的信息存储起来。
import urllib.request
from urllib.request import ProxyHandler,build_opener
import re
import random
import sqlite3
# 先设置要爬取网站的寄出网址
base_url = 'https://www.qiushibaike.com/hot/'
# 设置一个请求头列表
user_agent_list = ['Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)']
# 设置一个代理IP
ip_list = [{'http':'http://111.155.116.234:8123'},{'http':'http://183.167.217.152:63000'},{'http':'http://110.73.9.193:8123'}]

















