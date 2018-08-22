"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用cookie模拟登陆抽屉网进行点赞.PY
@ide:PyCharm
@time:2018-08-17 09:13:12
"""
import requests
class ChouTiSpider(object):
    def __init__(self):
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
            "Host":"dig.chouti.com",
            "Referer":"https://dig.chouti.com/",
            "Cookie":"gpsd=38c191a8421e552a39624a6c6a59d948; puid=026f80550b207bf398910ba13e36d916"
        }
        self.proxy = {"http":"http://41.65.111.229:8080"}
        self.session = requests.session()


    # 定义一个函数模拟登陆抽屉网
    def login(self):
        post_url = "https://dig.chouti.com/login"
        data={
            "oneMonth":"1",
            "password":"202325",
            "phone":"8613525517200"
        }
        response = self.session.post(post_url, proxies=self.proxy, data=data, headers = self.headers).json()
        print(response)

    # 定义一个点赞的函数
    def dianzan(self):
        response = self.session.post("https://dig.chouti.com/link/vote?linksId=21522206", headers = self.headers).json()
        print(response)

if __name__ == '__main__':
    spider = ChouTiSpider()
    spider.login()
    spider.dianzan()

