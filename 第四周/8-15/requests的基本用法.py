"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:requests的基本用法.PY
@ide:PyCharm
@time:2018-08-15 10:08:54
"""
import requests
# # 使用requests发起一个get请求
# response = requests.get('http://www.baidu.com')
# print(response)
# print(type(response))
# # 打印此次请求的地址
# print(response.url)
# # 打印此次请求的请求头
# print(response.headers)
# # 打印此次请求的cookie信息
# print(response.cookies)
# for key,value in response.cookies.items():
#     print(key,"=",value)
# # 打印此次请求的状态码
# print(response.status_code)
# # 获取网页内容
# # text：得到的是字符串
# print('========',response.text)
# # content：得到的是二进制数据
# print('1111111111111',response.content)


# ----------------使用requests构造一个携带参数的get请求----------
test_url_get ="http://httpbin.org/get"
params={
    "username":"zhangsan",
    "password":"123456"
}
# 使用requests发送请求如果不设置请求头，则默认的请求头是python-requests/requests版本号
response = requests.get(test_url_get,params=params)
print(response.text)
# # 当访问一个网址得到的是json字符串，则可以直接调用json（）函数，直接将返回的结果转换成字典可以直接解析json就不需要导入json模块，再使用json.loads()来进行转化了
print("=======",response.json())
print(type(response.json()))


# ----------使用requests构造一个携带参数的post请求-------------
test_url_get = "http://bin.org/post"
data = {
    "name":"lisi"
    "mima""678910"
}
response = requests.post(test_url_get,data=data)
print(response.text)



# --------------使用requests设置随机请求头和代理ip-------------------
# test_url = "http://httpbin.org/get"
# proxy = {'http':'http://219.141.153.41:80'}
# headers = {"User-Agent":"Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"}
# response = requests.get(test_url,proxies=proxy,headers=headers)
# print(response.text)

















