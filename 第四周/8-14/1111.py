"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:1111.PY
@ide:PyCharm
@time:2018-08-14 15:02:27
"""
import http.cookiejar
import urllib.request
from urllib.parse import urlencode
post_url = "https://dig.chouti.com/login"
post_data = urlencode({"oneMonth":"1","password":"202325","phone":"8613525517200"})
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0)"
}
def get_cookie():
    cookie_obj = http.cookiejar.MozillaCookieJar("chou_ti.txt")
    cookie_handler = urllib.request.HTTPCookieProcessor(cookie_obj)
    opener = urllib.request.build_opener(cookie_handler)
    data_bytes = bytes(post_data,encoding='utf-8')
    request = urllib.request.Request(post_url,data_bytes,headers)
    response = opener.open(request).read().decode('utf-8')
    print(response)
    cookie_obj.save(ignore_discard=True, ignore_expires=True)
# get_cookie()
def load_cookie():
    cookie = http.cookiejar.MozillaCookieJar()
    cookie.load("chou_ti.txt")
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    request = urllib.request.Request('https://dig.chouti.com/login',headers=headers)
    response = opener.open(request).read().decode('utf-8')
    print(response)
load_cookie()























