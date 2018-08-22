"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:1212.PY
@ide:PyCharm
@time:2018-08-17 14:35:05
"""
import requests
import random
import re
import json
class GuaZiSpider(object):
    user_agent_list = [
        'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
        'Mozilla/5.0Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
        'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11']
    # 设置一个代理IP
    ip_list = [{'https': 'https://49.81.19.117:23131'},
               {'http': 'http://180.113.29.212:61234'},
               {'https': 'https://118.252.64.196:27919'}]
    def __init__(self):
        self.base_url = 'http://car.qichedaquan.com/'
        self.headers = {
            'User-Agent':random.choice(self.user_agent_list),
        }
        self.ip = random.choice(self.ip_list)
        self.name_list = []

    def choose_name(self):
        response = requests.get(self.base_url,headers=self.headers).text
        # print(response)
        pattern = re.compile(r'<dl style="height: 259px;"><dt>(.*?)</dt>.*?<dt>(.*?)</dt>.*?<dt>(.*?)</dt>.*?<dt>(.*?)</dt>.*?<dt>(.*?)</dt>.*?<dt>(.*?)</dt>.*?<dt>(.*?)</dt>.*?<dt>(.*?)</dt>',re.S)
        choose_name = re.findall(pattern, response)
        for tuple in choose_name:
            for x in tuple:
                self.name_list.append(x)
        for index in range(0,len(self.name_list)):
            print(index+1,'.',self.name_list[index])

        self.get_qi_che(response)

    def get_qi_che(self,response):
        choose_name=int(input('请输入你选择的序号:'))
        pattern = re.compile(r'<dt>{}</dt>.*?>1</span>.*?href=.*?>(.*?)</a>.*?href=.*?>(.*?)</a>.*?href=.*?>(.*?)</a>.*?href=.*?>(.*?)</a>.*?href=.*?>(.*?)</a>.*?href=.*?>(.*?)</a>.*?href=.*?>(.*?)</a>'.format(self.name_list[choose_name]),re.S)
        result = re.findall(pattern,response)
        print(result)

if __name__ == '__main__':
    s = GuaZiSpider()
    s.choose_name()





















