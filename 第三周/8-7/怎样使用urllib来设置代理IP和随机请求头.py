"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:怎样使用urllib来设置代理IP和随机请求头.PY
@ide:PyCharm
@time:2018-08-07 14:14:47
"""
# 为什么设置代理IP和随机请求头？
# 爬虫默认的User-Agent（python-urllib/python版本）
# 1.服务器会判断一个频繁的请求是不是来自于同一个User-Agent标识，或者判断User-Agent是不是以python开头，如果是，则会限制访问。
# 解决方案：随机切换User-Agent的值。
# 2.服务器会判断一个频繁的请求是不是来自于同一个IP地址发出的，如果是，则会对IP进行限制访问。
# 解决方案：使用代理IP，随机切换IP地址，不使用真实的IP来发起请求。

import urllib.request
import random
# ----------------------使用urllib设置请求头-------------
# 定义一个要访问的网址：
# url = 'http://httpbin.org/get'
# # # 设置一个浏览器标识的列表(百度搜索user-agent,复制粘贴Mozilla/4.0的内容)
# user_agent_list = ['Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)']
# # 设置一个请求头（随机选择）
# headers = {
#     'User-Agent':random.choice(user_agent_list)
# }
# request = urllib.request.Request(url,headers=headers,method='GET')
# response = urllib.request.urlopen(request).read().decode('utf-8')
# print(response)


# 动态添加请求头
# result = urllib.request.Request(url,method='GET')
# result.addheader('User-agent','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)')
# response = urllib.request.urlopen(result)
# print(response.read().decode('utf-8'))



# ----------------使用urllib设置代理IP---------------
from urllib.request import ProxyHandler,build_opener
# 设置一个代理IP（百度西刺代理，ip、端口）
# ip_list = [{'http':'http://111.155.116.234:8123'},{'http':'http://183.167.217.152:63000'},{'http':'http://110.73.9.193:8123'}]
# # 创建一个IP代理对象
# proxy_handler = ProxyHandler(random.choice(ip_list))
# # 根据IP代理对象，创建用于发送请求的opener对象
# opener = build_opener(proxy_handler)
#
# # 再使用opener这个对象发起请求
# respose = opener.open('http://www.zhiyou100.com')
# print(respose.read().decode('utf-8'))




# ----------------使用urllib设置代理IP+随机请求头---------
# 定义一个要访问的网址：
url = 'http://httpbin.org/get'
# # 设置一个浏览器标识的列表(百度搜索user-agent,复制粘贴Mozilla/4.0的内容)
user_agent_list = ['Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)']
ip_list = [{'http':'http://111.155.116.234:8123'},{'http':'http://183.167.217.152:63000'},{'http':'http://110.73.9.193:8123'}]
# 设置一个请求头（随机选择）
headers = {
    'User-Agent':random.choice(user_agent_list)
}
request = urllib.request.Request(url,headers=headers,method='GET')

# 创建一个IP代理对象
proxy_handler = ProxyHandler(random.choice(ip_list))
# 根据IP代理对象，创建用于发送请求的opener对象
opener = build_opener(proxy_handler)
# 再使用opener这个对象发起请求
respose = opener.open(request)
print(respose.read().decode('utf-8'))













