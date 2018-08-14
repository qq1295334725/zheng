"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:空间.PY
@ide:PyCharm
@time:2018-08-13 19:35:08
"""
import urllib.request
from urllib.parse import urlencode
import json
import os
import time
import random
from urllib.request import ProxyHandler,build_opener
class KJSpider(object):
    user_agent_list = [
        'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
        'Mozilla/5.0Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
        'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11']
    # 设置一个代理IP
    ip_list = [{'http': 'http://111.155.116.235	:8123'}, {'http': 'http://61.135.217.7:80'},
               {'http': 'http://110.73.9.193:8123'}, {'https': 'https://101.132.122.230:3128'}]
    def __init__(self,qq,fang_wen_qq):
        self.headers = {'User-Agent':random.choice(self.user_agent_list)}
        self.ip = random.choice(self.ip_list)
        self.base_url = "https://h5.qzone.qq.com/proxy/domain/photo.qzone.qq.com/fcgi-bin/cgi_floatview_photo_list_v2?"
        self.qq = qq
        self.fang_wen_qq = fang_wen_qq
    def get_page(self):
        # 设置访问网址的键值对
        params = {
            "g_tk":776011230,
            "callback":"viewer_Callback",
            "t":455717206,
            "topicId":"V13LWQts0VPfSK",
            "picKey":"NDR0Vq0mL2C1Fln8EiUvbAEAAAAAAAA!",
            "shootTime":'',
            "cmtOrder":1,
            "fupdate":1,
            "plat":"qzone",
            "source":"qzone",
            "cmtNum":10,
            "likeNum":5,
            "inCharset":"utf-8",
            "outCharset":"utf-8",
            "callbackFun":"viewer",
            "offset":0,
            "number":15,
            "uin":self.fang_wen_qq,
            "appid":4,
            "isFirst":1,
            "hostUin":self.qq,
            "sortOrder":1,
            "showMode":1,
            "need_private_comment":1,
            "prevNum":9,
            "postNum":18,
            "_":str(time.time()).replace('.','')[0:13]
        }
        url = self.base_url + urlencode(params)
        request = urllib.request.Request(url, headers=self.headers)
        ip_proxyhandler = ProxyHandler(self.ip)
        opener = build_opener(ip_proxyhandler)
        urllib.request.install_opener(opener)
        try:
            response = urllib.request.urlopen(request)
            if response.status == 200:
                html = response.read().decode('utf-8')
                print(html)
                # 调用parse_json来解析json数据
                # self.parse_json(html)

        except Exception as e:
            return None
        # 定义一个函数来解析json


    # def parse_json(self, html):
    #     json_data = json.loads(html)

if __name__ == '__main__':
    s = KJSpider(791063894,1295334725)
    s.get_page()




















