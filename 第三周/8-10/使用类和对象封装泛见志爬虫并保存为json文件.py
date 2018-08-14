"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用类和对象封装泛见志爬虫并保存为json文件.PY
@ide:PyCharm
@time:2018-08-10 09:27:57
"""
import urllib.request
from urllib.request import ProxyHandler,build_opener
import random
import json
import re
class FJZSpider(object):
    user_agent_list = [
'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50','Mozilla/5.0Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1','Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11']
    # 设置一个代理IP
    ip_list = [{'http': 'http://111.155.116.235	:8123'}, {'http': 'http://61.135.217.7:80'},
{'http': 'http://110.73.9.193:8123'}, {'https': 'https://101.132.122.230:3128'}]
    def __init__(self):
        self.base_url = 'http://www.fanjian.net/duanzi'
        self.headers = {'User-Agent':random.choice(self.user_agent_list)}
        self.ip = random.choice(self.ip_list)
        self.big_list=[]

    # 定义一个函数来获取总页数
    def get_total_page_num(self):
        request = urllib.request.Request(self.base_url,headers=self.headers)
        ip_proxyhandler = ProxyHandler(self.ip)
        opener = build_opener(ip_proxyhandler)
        # 将opener对象设置为全局的，让整个文件都可以使用opener对象
        urllib.request.install_opener(opener)
        # 再使用urllib.request.urlopen打开一个网址的时候，就相当于使用了opener对象在打开网址
        response = urllib.request.urlopen(request).read().decode('utf-8')
        pattern_obj=re.compile(r'共(.*?)页',re.S)
        total_num = int(re.search(pattern_obj,response)[1])
        self.get_total_info(total_num)
    # 定义一个函数来获取每一页的详细信息
    def get_total_info(self, total_num):
        for page in range(1, total_num+1):
            print('正在爬取第{}页...'.format(page))
            abs_url = self.base_url+"-"+str(page)
            request = urllib.request.Request(url=abs_url,headers=self.headers)
            response = urllib.request.urlopen(request).read().decode('utf-8')
            pattern_obj=re.compile(r'<a.*?class="cont-list-editor">(.*?)</a>.*?<p>(.*?)</p>.*?</em>(.*?)</a>.*?浏览.*?</span>(.*?)<span class="sp">.*?时间.*?</span>(.*?)<span class="sp">',re.S)
            result_list = re.findall(pattern_obj, response)
            self.change_to_json(result_list)
    # 定义一个函数来处理匹配到的result_list
    def change_to_json(self,result_list):
        for nick_name,content,tu_cao,look_num,publish_time in result_list:
            dict_info={"用户昵称:":nick_name,"段子内容:":content,"吐槽:":tu_cao,"浏览量:":look_num,"发表时间:":publish_time}
            self.big_list.append(dict_info)

    # 定义一个函数来存储数据
    def save_to_json(self):
        result_list = json.dumps(self.big_list)
        f = open('泛见志.txt','w',encoding='utf-8')
        f.write(result_list)
        f.close()
    # 定义一个开始函数，让爬虫启动起来
    def start_spider(self):
        self.get_total_page_num()
        self.save_to_json()

if __name__ == '__main__':
    spider = FJZSpider()
    spider.start_spider()

# xpath BeautifulSoup,requests












