"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:爬虫练习段子.PY
@ide:PyCharm
@time:2018-08-20 19:17:36
"""
import requests
import random
from lxml import etree
import re
class DuanZiSider(object):
    user_agent_list = [
        'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
        'Mozilla/5.0Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
        'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11']
    # 设置一个代理IP
    ip_list = [{'http':'http://113.90.247.90:8118'},
               {'https': 'https://60.168.96.156:8123'},
               {'http': 'http://220.191.13.135:6666'}]
    def __init__(self):
        self.base_url = 'http://jandan.net/duan'
        self.ip = random.choice(self.ip_list)
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Referer':'http://jandan.net/duan',
            'Host':'jandan.net'
        }
        self.headers_1 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0',
        }
        self.list=[]
        self.big_list=[]

    # 获取页码
    def page_duan_zi(self):
        response = requests.get(self.base_url, headers=self.headers_1).text
        # print(response)
        html = etree.HTML(response)
        # print(html)
        num =html.cssselect('span[class="current-comment-page"]')[0].text
        page_num = int(str(num)[1:3])
        print(page_num)
        self.get_duan_zi(page_num)

    # 发起get请求
    def get_duan_zi(self,page_num):
        for x in range(0,page_num):
            page = page_num-x
            print('正在爬取第{}页...'.format(page))
            url = self.base_url+'/page-'+str(page)
            response = requests.get(url, headers=self.headers).text
            html = etree.HTML(response)
            # 获取名字
            text1 = html.cssselect('strong')
            for x in range(1,len(text1)):
                text1=html.cssselect('strong')[x].text
                self.list.append(text1)
            # 获取文本
            text = html.xpath("//p/text()")[3:-4]
            self.write_duan_zi(text1,text)



    def write_duan_zi(self,text1,text):
        f = open('duanzi.txt', 'a+', encoding='utf-8')
        # for x in range(0, len(text1)):
        for y in range(0,len(text)):
                # f.write('段子手：{}'.format(text1[x]))
                # f.write('\n')
            f.write('正文：{}'.format(text[y]))
            f.write('\n')
            f.write('--------------')
            f.write('\n')


if __name__ == '__main__':
    s = DuanZiSider()
    s.page_duan_zi()


