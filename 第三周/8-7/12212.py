"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:12212.PY
@ide:PyCharm
@time:2018-08-07 19:24:58
"""
import urllib.request
# res = urllib.request.urlopen('http://www.baidu.com')
# print(res.read().decode('utf-8'))

import urllib.parse
# base_url = 'http://www.yundama.com/index/login'
# data_dict = {
#     "username":"1235456",
#     "password":"4564652",
#     'utype':"1",
#     "vcode":"seww"
# }
# data_string = urllib.parse.urlencode(data_dict)
# print(data_string)
# new_url = base_url+'?'+data_string
# response = urllib.request.urlopen(new_url)
# print(response.read().decode('utf-8'))

# http://api.map.baidu.com/telematics/v3/weather?location=郑州市&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?
# res_base = 'http://api.map.baidu.com/telematics/v3/weather'
# date1 = {
#     "location":"郑州市",
#     "output":"json",
#     "ak":"TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ",
#     "callback":"?"
# }
# string1 = urllib.parse.urlencode(date1)
# new_string = res_base+'?'+string1
# response = urllib.request.urlopen(new_string)
# print(response.read().decode('utf-8'))
#
# city = urllib.request.quote('郑州市'.encode('utf-8'))
# response = urllib.request.urlopen('http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'.format(city))
# print(response.read().decode('utf-8'))
#
# # post
# data_dict = {"username":"zhangsan","password":"123456"}
# data_string = urllib.parse.urlencode(data_dict)
# last_data = bytes(data_string,encoding='utf-8')
# response = urllib.request.urlopen("http://httpbin.org/post",data=last_data)
# print(response.read().decode('utf-8'))

import urllib.request
import urllib.parse
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# user_base = 'http://www.yundama.com/index/login'
# data_dict = {
#     "username":"454545",
#     "password":"412122",
#     "utype":"1",
#     "vcode":"dsff"
# }
# data_string = urllib.parse.urlencode(data_dict)
# new_string = user_base+'?'+data_string
# response = urllib.request.urlopen(new_string)
# print(response.read().decode('utf-8'))

# post
# data_dict = {"username":"zhangsan","password":"1123122"}
# data_string = urllib.parse.urlencode(data_dict)
# user_string = bytes(data_string.encode('utf-8'))
# response = urllib.request.urlopen('http://httpbin.org/post',data=user_string)
# print(response.read().decode('utf-8'))

import random
# url = 'http://httpbin.org/get'
# user_agent_list = ['MQQBrowser/26Mozilla/5.0(Linux;U;Android2.3.7;zh-cn;MB200Build/GRJ22;CyanogenMod-7)AppleWebKit/533.1(KHTMLlikeGecko)Version/4.0MobileSafari/533.1','Opera/9.80(Android2.3.4;Linux;OperaMobi/build-1107180945;U;en-GB)Presto/2.8.149Version/11.10']
# headers = {
#     'User-Agent':random.choice(user_agent_list)
# }
# response = urllib.request.Request(url,headers=headers,method='GET')
# res = urllib.request.urlopen(response).read().decode('utf-8')
# print(res)

import re
from urllib.request import ProxyHandler,build_opener
ip_list = [{"http":"http://61.135.217.7:80"},{"http":"118.190.95.35:9001"}]
proxy_handler = ProxyHandler(random.choice(ip_list))
opener = build_opener(proxy_handler)
response = opener.open('http://www.zhiyou100.com').read().decode('utf-8')


pattern_obj = re.compile('(http.+index)')
res = re.findall(pattern_obj,response)
print(res[0])









