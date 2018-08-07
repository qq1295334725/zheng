"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用urllib库发送get和post请求.PY
@ide:PyCharm
@time:2018-08-07 10:08:09
"""
# urllib是python中内置的发送网络请求的一个库（包），在Python2中由urllib和urllib2两个库来实现请求的发送，但是Python中已经不存在urllib2这个库了，已经将urllib和urllib2合并为urllib。
# urllib是一个库（包），request是urllib库里面用于发送网络请求 的一个模块。
import urllib.request
# 发起一个不携带参数的get请求
# responce = urllib.request.urlopen('http://www.baidu.com')
# 调用status属性可以此次请求响应的状态码，200表示此次请求成功。
# print(responce.reason)
# print(responce.status)
# 调用url属性，可以获取此次请求的地址
# print(responce.url)
# print(responce.headers)
# 由于使用read方法拿到的响应的数据是二进制数据，所有需要使用decode解码成utf-8编码。
# print(responce.read().decode('utf-8'))

# -----------构造一个携带参数的请求--------------
import urllib.parse
# http://www.yundama.com/index/login?username=gaghdfsg&password=44656556&utype=1&vcode=rqrwer

# 定义出来基础网址
# base_url = 'http://www.yundama.com/index/login'
# 构造一个字典
# data_dict = {
#     "username":"gaghdfsg",
    # "password":"44656556",
#     "utype":"1",
#     "vcode":"rqrwer"
# }
# 使用urlencode这个方法将字典序列化成字符串，做好和基础网址进行拼接
# data_string = urllib.parse.urlencode(data_dict)
# print(data_string)
# new_url = base_url+'?'+data_string
# response = urllib.request.urlopen(new_url)
# print(response.read().decode('utf-8'))


# http://api.map.baidu.com/telematics/v3/weather?location=郑州市&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?
# base_url = 'http://api.map.baidu.com/telematics/v3/weather'
# data_dict = {
#     "location":"郑州市",
#     "output":"json",
#     "ak":"TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ",
#     "callback":"?"
# }
# data_string = urllib.parse.urlencode(data_dict)
# print(data_string)
# new_url = base_url+'?'+data_string
# response = urllib.request.urlopen(new_url)
# print('11111111',response.read().decode('utf-8'))



# 如果直接将中文传入URL中请求(使用urllib.request.urlopen直接访问网址时)，会导致编码错误，我们需要使用quote，对该中文关键字进行URL编码。
# city = urllib.request.quote('郑州市'.encode('utf-8'))
# response = urllib.request.urlopen(('http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?').format(city))
# print(response.read().decode('utf-8'))


# ------------构造一个携带参数的POST请求-------------
# 测试网址：http://httpbin.org/post
# 定义一个字典参数
data_dict = {"username":"zhangsan","password":"123456"}
# 使用urlencode将字典参数序列化成字符串
data_string = urllib.parse.urlencode(data_dict)
# 将序列化后的字符串转换成二进制参数，因为post请求携带的是二进制参数
last_data = bytes(data_string,encoding='utf-8')
# 如果给urlopen这个参数传递给了data这个参数，那么它的请求方式则不是get请求，而是post请求
response = urllib.request.urlopen("http://httpbin.org/post",data=last_data)
# 我们的参数出现在form表单中，着表明是模拟了表单的提交方式，以post方式传输数据
print(response.read().decode('utf-8'))

