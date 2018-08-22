"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:1122.PY
@ide:PyCharm
@time:2018-08-13 20:24:42
"""
import requests
import json
from urllib.parse import urlencode
class JPMTSpider(object):
    def __init__(self,keyword):
        self.headers = {"User-Agent":'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'}
        self.base_url = 'https://www.toutiao.com/search_content/?'
        self.session = requests.Session()
        self.keyword = keyword
    # get请求
    def get_mei_tu(self):
        self.parms = {
            "offset": 20,
            "format": "json",
            "keyword": self.keyword,
            "autoload": "true",
            "count": 20,
            "cur_tab": 1,
            "from": "search_tab"
        }
        url = self.base_url+urlencode(self.parms)
        response = self.session.get(url,headers=self.headers).json()
        print(type(response))
        print(response)
    #     self.qu_tu_pian(response)
    #
    # # 取图片网址
    # def qu_tu_pian(self,response):
    #     html_data = json.loads(response)
    #     print(html_data)












if __name__ == '__main__':
    jpmt=JPMTSpider('街拍美图')
    jpmt.get_mei_tu()


