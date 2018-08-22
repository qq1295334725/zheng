"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用requests和cookie模拟登陆github.PY
@ide:PyCharm
@time:2018-08-15 14:23:17
"""
#  要做模拟登陆需要知道表单数据的提交地址，和提交的数据，经观察发现点击登陆发起的是一个post请求，请求的地址是https://github.com/session，提交的参数中commit，utf-8这两个参数是不会变化的，login这个参数是自己填写的账户名，password这个参数是自己添加的密码，剩下的就是这个authenticity_token这个参数它是一个加密参数。经过分析authenticity_token这个参数是在登录页面源代码里面可以找到，也就是说只要访问登录页面拿到源代码就可以获取authenticity_token这个参数的值。到目前为止，五个参数的值都可以拿到，下面就可以模拟登陆。#
import requests
import re
class Login_GitHub(object):
    def __init__(self):
        self.headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
            "Host":"github.com",
            "Referer":"https://github.com/"
        }
        self.login_url="https://github.com/login"
        self.post_url="https://github.com/session"
        self.logined_url = "https://github.com/settings/profile"
        self.session=requests.Session()

    #定义一个函数来获取authenticity_token这个参数的值
    def get_authenticity_token(self):
        response=self.session.get(self.login_url,headers=self.headers).text
        pattern_obj=re.compile(r'authenticity_token.*?value="(.*?)" />',re.S)
        authenticity_token=re.search(pattern_obj,response)[1]
        return authenticity_token

    #拿到authenticity_token这个参数就可以进行模拟登陆了
    def login(self,login,password):
        post_data={
            "commit":"Sign+in",
            "utf8":"√",
            "authenticity_token":self.get_authenticity_token(),
            "login":login,
            "password":password,
        }
        self.session.post(self.post_url,data=post_data,headers=self.headers)
        response=self.session.get(self.logined_url,headers=self.headers).text
        self.profile(response)
    def profile(self, html):
        pattern_obj = re.compile(r'<input class="form-control" type="text" value="(.*?)".*?id="user_profile_name" />',re.S)
        name = re.search(pattern_obj, html)[1]
        print(name)



if __name__ == '__main__':
    github = Login_GitHub()
    # github.get_authenticity_token()
    github.login("xiaochideid","chi152900")
















