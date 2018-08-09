"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用类和对象封装百度精品贴爬虫.PY
@ide:PyCharm
@time:2018-08-09 15:54:56
"""
import re
import urllib.request
from urllib.request import ProxyHandler,build_opener,quote
from 模块调用 import BDTBSpider
class JPTSpider(BDTBSpider):
    # tie_ba_name是贴吧的名字，创建 JPTSpider类生成的对象的时候，会给这个形参传值
    def __init__(self,tie_ba_name):
        super(JPTSpider,self).__init__(tie_ba_id='')
        self.url ='https://tieba.baidu.com/f?kw={}&ie=utf-8&tab=good'.format(quote(tie_ba_name))
    # 定义一个函数用来获取所有精品帖子的个数
    def get_total_tie_zi_num(self):
        # self.headers是从父类 BDTBSpider里面继承过来的
        request = urllib.request.Request(url=self.url,headers=self.headers)
        ip_proxyhandler = ProxyHandler(self.ip)
        opener = build_opener(ip_proxyhandler)
        response = opener.open(request).read().decode('utf-8')
        pattern_obj = re.compile(r'<span class="red_text">(.*?)</span>',re.S)
        # 获取精品帖子的个数
        total_num = int(re.search(pattern_obj,response)[1])
        self.get_tie_zi_id(total_num)

    # 获取所有帖子的id
    def get_tie_zi_id(self,total_num):
        for page in range(0,total_num,50):
            abs_url = self.url+"&cid=0&pn={}".format(str(page))
            request = urllib.request.Request(url=abs_url, headers=self.headers)
            ip_proxyhandler = ProxyHandler(self.ip)
            opener = build_opener(ip_proxyhandler)
            response = opener.open(request).read().decode('utf-8')
            pattern_obj=re.compile(r'<a.*?href="/p/(.*?)".*?class="j_th_tit ',re.S)
            result_list = re.findall(pattern_obj,response)
            for id in result_list:
                print('正在爬取帖子id为{}的帖子信息'.format(id))
                # 将每一个id都传给 BDTBSpider这个类
                bd = BDTBSpider(id)
                bd.start_spider()

    def jpt_start_spider(self):
        # 调用父类函数中的启动函数
        self.get_total_tie_zi_num()

if __name__ == '__main__':
    jpt = JPTSpider('英雄联盟')
    jpt.jpt_start_spider()





