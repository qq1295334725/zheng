"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用urllib和cookie模拟登陆智游教务管理系统.PY
@ide:PyCharm
@time:2018-08-14 14:13:16
"""
# 1.分析智游教务管理系统的请求，找到登录按钮请求到的地址，分析发现是一个post请求，请求到的地址是http://kaoshi.zhiyou900.com:8888/edustu/login/login.spr，请求携带了两个参数：j_password，j_username
# 2.编写代码模拟发送一个携带参数的post请求登录网页，然后拿到登陆成功之后的cookie信息保存到本地
# 3.下次登录的时候只需要携带上本地的cookie信息即可完成登录。
import http.cookiejar
import urllib.request
from urllib.parse import urlencode
# 定义发起post请求的url地址
post_url = "http://kaoshi.zhiyou900.com:8888/edustu/login/login.spr"
# 构造参数：
post_data = urlencode({"j_username":"13525517200","j_password":"123456"})
# 设置一个请求头
headers={
    "User-Agent":"Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
}
# 定义参数来获取cookie信息
def get_cookie():
    # 创建一个MozillaCookieJar的对象
    cookie_obj = http.cookiejar.MozillaCookieJar("stu_cookie.txt")
    # 根据cookie_obj对象创建一个用于管理cookie信息的操作对象handler
    cookie_handler = urllib.request.HTTPCookieProcessor(cookie_obj)
    # 根据cookie_handler创建一个opener对象
    opener = urllib.request.build_opener(cookie_handler)
    # 对post_url发起请求
    data_bytes = bytes(post_data,encoding='utf-8')
    # 创建一个request对象
    request = urllib.request.Request(post_url,data_bytes,headers)
    # 根据opener对象来发起请求
    response = opener.open(request).read().decode('utf-8')
    print(response)
    # 登陆成功之后将服务器返回的cookie信息保存到本地
    cookie_obj.save(ignore_discard=True, ignore_expires=True)
get_cookie()
def load_cookie():
    cookie = http.cookiejar.MozillaCookieJar()
    cookie.load("stu_cookie.txt",ignore_expires=True, ignore_discard=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    request = urllib.request.Request("http://kaoshi.zhiyou900.com:8888/edustu/me/edu/meda.spr",headers=headers)
    response = opener.open(request).read().decode('utf-8')
    # print(response)
# load_cookie()











