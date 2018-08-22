"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:5445.PY
@ide:PyCharm
@time:2018-08-15 19:37:07
"""
import urllib.request
import http.cookiejar
from urllib.parse import urlencode
class ZhiYou(object):
    def __init__(self):
        self.post_url = "http://kaoshi.zhiyou900.com:8888/edustu/login/login.spr"
        # 构造参数：
        self.post_data = urlencode({"j_username": "13525517200", "j_password": "123456"})
        # 设置一个请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
        }

    def cookie_save(self):
        pass
















if __name__ == '__main__':
    zhi = ZhiYou()
    zhi.cookie_save()











