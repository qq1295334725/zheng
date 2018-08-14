"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:121221.PY
@ide:PyCharm
@time:2018-08-09 17:40:27
"""
import re
import random
import urllib.request
from urllib.request import ProxyHandler,build_opener
class QSBKWenZi(object):
    user_agent_list = ['Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
                       'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)',
                       'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
                       'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)']
    # 设置一个代理IP
    ip_list = [{'http': 'http://111.155.116.234:8123'}, {'http': 'http://183.167.217.152:63000'},
               {'http': 'http://110.73.9.193:8123'}]
    def __init__(self,text_id):
        self.text = text_id
        self.url_base = 'https://www.qiushibaike.com/{}'.format(self.text)+'/'
        self.headers = {'User-Agent':random.choice(self.user_agent_list)}
        self.ip = ProxyHandler(random.choice(self.ip_list))

    def all_base_page(self):
        request = urllib.request.Request(url=self.url_base,headers=self.headers)
        opener = build_opener(self.ip)
        response = opener.open(request).read().decode('utf-8')
        patter_obj = re.compile(r'<a href="/text/page/13/".*?<span class="page-numbers">(.*?)</span>',re.S)
        all_page = int(re.search(patter_obj, response)[1])
        print(all_page)
        self.total_spide(all_page)
    def total_spide(self,all_page):
        for page in range(1,all_page+1):
            print('正在爬取第{}页......'.format(page))
            all_url_base = self.url_base+str(all_page)+'/'
            request = urllib.request.Request(url=all_url_base,headers=self.headers)
            opener = build_opener(self.ip)
            response = opener.open(request).read().decode('utf-8')
            pattern_obj = re.compile(
                r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?class="articleGender .*?Icon">(.*?)</div>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats">.*?<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>',
                re.S)
            content_all = re.findall(pattern_obj, response)
            self.remove_string(content_all)
    def remove_string(self,content_all):
        remove_n = re.compile(r'\n',re.S)
        remove_br = re.compile(r'<br/>', re.S)
        for tobal_list in content_all:
            file_name = re.sub(remove_n,'',tobal_list[0])
            age = tobal_list[1]
            content = re.sub(remove_n,'',tobal_list[2])
            content = re.sub(remove_br,'',content)
            file_hao_xiao = tobal_list[3]
            file_review = tobal_list[4]
            tobal_list = (file_name,age,content,file_hao_xiao,file_review)
            self.file_txt(tobal_list)
    def file_txt(self,tobal_list):
        file_test = open('QSBKTest.txt','a+',encoding='utf-8')
        file_test.write('用户昵称:{}'.format(tobal_list[0]))
        file_test.write('\n')
        file_test.write('年龄:{}'.format(tobal_list[1]))
        file_test.write('\n')
        file_test.write('内容:{}'.format(tobal_list[2]))
        file_test.write('\n')
        file_test.write('好笑数:{}'.format(tobal_list[3]))
        file_test.write('\n')
        file_test.write('用户评论:{}'.format(tobal_list[4]))
        file_test.write('\n')
        file_test.write('-----------下一个-------------')
        file_test.write('\n')

if __name__ == '__main__':
    spider = QSBKWenZi('text')
    spider.all_base_page()
























