"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:西刺代理爬虫.PY
@ide:PyCharm
@time:2018-08-11 08:59:59
"""
import urllib.request
import re
import random
from urllib.request import ProxyHandler,build_opener
class XIDLip(object):
    user_agent_list = [
        'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
        'Mozilla/5.0Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
        'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11']
    # 设置一个代理IP
    ip_list = [{'http': 'http://111.155.116.235	:8123'}, {'http': 'http://61.135.217.7:80'},
               {'http': 'http://110.73.9.193:8123'}, {'https': 'https://101.132.122.230:3128'}]
    def __init__(self):
        self.url = 'https://blog.csdn.net/u012195214/article/details/78889602'
        self.headers = {'User-Agent':random.choice(self.user_agent_list)}
        self.ip = random.choice(self.ip_list)
    # 爬取数据内容
    def headers_pc_pa_chong(self):
        print('正在爬取')
        request = urllib.request.Request(url=self.url,headers=self.headers)
        ip_proxyhandler = ProxyHandler(self.ip)
        opener = build_opener(ip_proxyhandler)
        response = opener.open(request).read().decode('utf-8')
        pattern_obj = re.compile(r'<li><strong>PC端：</strong>.*?</ul>(.*?)<ul>',re.S)
        list_1 = re.findall(pattern_obj,response)
        list_2=''.join(list_1)
        pattern_obj_1 = re.compile(r'<p>(.*?)<br>(.*?)</p>',re.S)
        pc_headers_list = re.findall(pattern_obj_1, list_2)

        self.remove_pc(pc_headers_list)
    # 删除多余的空格\n
    def remove_pc(self,pc_headers_list):
        remove_n = re.compile(r'\n', re.S)
        remove_user = re.compile(r'User-Agent:',re.S)
        for x, y in pc_headers_list:
            user1 = re.sub(remove_n,'', y)
            user1 = re.sub(remove_user, '', user1)
            new_headers = (x,user1)
            self.cun_chu_heardes(new_headers)
    # 存储数据
    def cun_chu_heardes(self,new_headers):
        f = open('User-Agent.txt', 'a+', encoding='utf-8')
        f.write('浏览器类型为：{}'.format(new_headers[0]))
        f.write('\n')
        f.write("'{}'".format(new_headers[1]))
        f.write('\n')
        f.write('----------------------------')
        f.write('\n')
    def start_def(self):
        self.headers_pc_pa_chong()
if __name__ == '__main__':
    res = XIDLip()
    res.start_def()


























