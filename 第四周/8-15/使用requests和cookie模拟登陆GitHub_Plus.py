"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用requests和cookie模拟登陆GitHub_Plus.PY
@ide:PyCharm
@time:2018-08-15 20:26:01
"""
import requests
import re
import http.cookiejar
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
        #给session对象设置一个cookies属性
        self.session.cookies=http.cookiejar.MozillaCookieJar("git_hub.txt")

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
        #模拟登陆完成之后给cookie信息保存下来
        self.session.cookies.save(ignore_discard=True, ignore_expires=True)


    def profile(self):
        #下次再爬取的时候直接加载cookie信息进行爬取即可
        self.session.cookies.load("git_hub.txt",ignore_discard=True, ignore_expires=True)
        response = self.session.get(self.logined_url, headers=self.headers).text
        pattern_obj = re.compile(r'<input class="form-control" type="text" value="(.*?)".*?id="user_profile_name" />',re.S)
        name = re.search(pattern_obj, response)[1]
        print(name)

if __name__ == '__main__':
    github=Login_GitHub()
    # github.get_authenticity_token()
    # github.login("自己的账号","自己的密码")
    github.profile()














