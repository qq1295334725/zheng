"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用云打码平台实现验证码的识别.PY
@ide:PyCharm
@time:2018-08-16 09:35:05
"""
from YDMHTTP8月16Demo3 import yan_zheng
import requests

class YunDaMaSpider(object):
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"}
        self.session = requests.Session()
        self.file_name = "captcha.jpeg"
    # 定义一个函数获取验证码图片
    def get_captcha(self):
        response = self.session.get("http://www.yundama.com/index/captcha",headers=self.headers)
        # 把图片存到了本地
        with open(self.file_name,'wb') as f:
            f.write(response.content)


    # 定义一个函数来进行模拟登录
    def login_ydam(self):
        # 先调用 get_captha（）函数把验证码存到本地
        self.get_captcha()
        # 将验证码图片传到yan_zheng这个函数中，识别的结果result
        cid,result = yan_zheng(self.file_name)
        # 手动识别
        # result=input('请输入验证码：')
        response=self.session.get("http://www.yundama.com/index/login?username=cp135255172&password=llchen@06.23.&utype=1&vcode={}".format(result),headers=self.headers).json()
        res = response["ret"]
        if res==0:
            print("模拟登陆成功了！")

if __name__ == '__main__':
    yundama=YunDaMaSpider()
    yundama.login_ydam()












