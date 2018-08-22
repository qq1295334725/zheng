"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:作业.PY
@ide:PyCharm
@time:2018-08-17 14:20:10
"""
import requests
import re
import random
from urllib.parse import urlencode
class XiaoShuoSpider(object):
    user_agent_list = [
        'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
        'Mozilla/5.0Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
        'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11']
    # 设置一个代理IP
    ip_list = [{'https':'https://49.81.19.117:23131'},
{'http':'http://180.113.29.212:61234'},
{'https':'https://118.252.64.196:27919'}]
    def __init__(self):
        self.base_url = 'http://top.kanshu.com/list_7_1.html'
        self.headers = {
            "User-Agent":random.choice(self.user_agent_list)
        }
        self.proxy = random.choice(self.ip_list)
        self.session = requests.session()

    def get_xiao_shuo(self):
        '''
        获取首页的源代码
        :return:
        '''
        for page_num in range(1,7):
            print('正在爬取第{}页.......'.format(page_num))
            parms_data = {
                    "is_ajax":"1",
                    "page":page_num,
                    "timeType":"week",
                    "big_id":"7"
            }
            url = self.base_url+'?'+urlencode(parms_data)
            response_data = self.session.get(url,headers=self.headers,proxies=self.proxy).json()
            self.get_nei_rong(response_data)

    def get_nei_rong(self,response_data):
        '''
        匹配首页的小说网址
        :param response_data:
        :return:无
        '''
        result = response_data['result']
        data = result['data']
        html_str = data['html']
        pattern_obj = re.compile(r'<span class="sp_03"><a href="(.*?)">',re.S)
        response = re.findall(pattern_obj,html_str)
        self.xin_xi(response)

    def xin_xi(self, response):
        '''
        进入每个小说的网站，获取每个小说的源代码，并且匹配需要的内容
        :param response: 每个小说的网址
        :return:
        '''
        for url in response:
            result = requests.get(url,headers = self.headers,proxies=self.proxy).content.decode('gb18030')
            pattern = re.compile(r'<div class="div1">.*?<h1>(.*?)</h1>.*?<div class="xx_xinx">.*?<li>作品分类：.*?>(.*?)</span>.*?授权状态.*?>(.*?)</span>.*?写作进程.*?>(.*?)</span>.*?总 字 数.*?>(.*?)</span>.*?总 点 击.*?>(.*?)</span>.*?本月点击.*?>(.*?)</span>.*?<p class="top_stat">.*?>(.*?)</b>',re.S)
            response_1 = re.findall(pattern,result)
            self.save_xin_xi(response_1)

    def save_xin_xi(self,response_1):
        for tuple_big in response_1:
            f = open('xiaoshuo.txt','a+',encoding='utf-8')
            f.write('作品名称：{}'.format(tuple_big[0]))
            f.write('\n')
            f.write('作品分类：{}'.format(tuple_big[1]))
            f.write('\n')
            f.write('授权状态：{}'.format(tuple_big[2]))
            f.write('\n')
            f.write('写作进程：{}'.format(tuple_big[3]))
            f.write('\n')
            f.write('总字数：{}'.format(tuple_big[4]))
            f.write('\n')
            f.write('总点击：{}'.format(tuple_big[5]))
            f.write('\n')
            f.write('本月点击：{}'.format(tuple_big[6]))
            f.write('\n')
            f.write('总阅读：{}'.format(tuple_big[7]))
            f.write('\n')
            f.write('----------------------------------')
            f.write('\n')


if __name__ == '__main__':
    s = XiaoShuoSpider()
    s.get_xiao_shuo()




