"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用requests和cookie模拟登陆智游教务管理系统.PY
@ide:PyCharm
@time:2018-08-15 11:32:41
"""
import requests
class LoginZhiYou(object):
    def __init__(self):
        self.post_url = "http://kaoshi.zhiyou900.com:8888/edustu/login/login.spr"
        self.headers = {"User-Agent":"Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"}
        self.session = requests.Session()
    def login(self,username,password):
        data = {
            'j_username':username,
            'j_password':password
        }
        response = self.session.post(self.post_url,data=data,headers = self.headers)
        print(response.text)
    def is_login(self):
        response = self.session.get("http://kaoshi.zhiyou900.com:8888/edustu/me/edu/meda.spr",headers=self.headers)
        if response.status_code==200:
            print("登录状态:",response.text)
        else:
            print("非登录状态")
if __name__ == '__main__':
    zhiyou = LoginZhiYou()
    zhiyou.login("13525517200","123456")
    zhiyou.is_login()


