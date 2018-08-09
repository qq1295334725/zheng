"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:练习泛见志.PY
@ide:PyCharm
@time:2018-08-09 15:52:19
"""
import re
import random
import urllib.request
from urllib.request import ProxyHandler,build_opener
class FJZDuanZi(object):
    user_agent_list = [
        'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
        'Mozilla/5.0Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
        'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11']
    # 设置一个代理IP
    ip_list = [{'http': 'http://111.155.116.235	:8123'}, {'http': 'http://61.135.217.7:80'},
               {'http': 'http://110.73.9.193:8123'}, {'https': 'https://101.132.122.230:3128'}]
    def __init__(self,duan_zi):
        self.duan_zi = duan_zi
        self.url_base = 'http://www.fanjian.net/{}'.format(duan_zi)
        self.headers = {'User-Agent':random.choice(self.user_agent_list)}
        self.ip = random.choice(self.ip_list)

    def all_page(self):
        request = urllib.request.Request(url=self.url_base,headers=self.headers)
        proxy_handler = ProxyHandler(self.ip)
        opener = build_opener(proxy_handler)
        response = opener.open(request).read().decode('utf-8')
        patter_obj = re.compile(r'<span class="fc-gray">共(.*?)页',re.S)

        all_page_1 = int(re.search(patter_obj, response)[1])
        # print(all_page_1)
        self.pa_qu_duan_zi(all_page_1)
    def pa_qu_duan_zi(self, all_page_2):
        for page_num in range(1,all_page_2+1):
            print('正在爬取第{}页，请稍候'.format(page_num))
            url_base = self.url_base+'-'+str(page_num)
            request = urllib.request.Request(url=url_base,headers=self.headers)
            ip_proxy_handler = ProxyHandler(self.ip)
            opener = build_opener(ip_proxy_handler)
            response = opener.open(request).read().decode('utf-8')
            patter_obj = re.compile(r'<div class="cont-list-reward".*?title="(.*?)".*?<p>(.*?)</p>.*?</em>(.*?)</a>.*?title="浏览".*?</span>(.*?)<span class="sp">.*?title="时间".*?</span>(.*?)<span class="sp"',re.S)
            total_duan_zi = re.findall(patter_obj,response)
            # print(total_duan_zi)
            self.remove_kong(total_duan_zi)
    def remove_kong(self,total_duan_zi):
        remove_kong = re.compile(r' ',re.S)
        for tuple_data in total_duan_zi:
            tile_name = tuple_data[0]
            tile = tuple_data[1]
            if ' ' in tuple_data[2]:
                comment = re.sub(remove_kong,'',tuple_data[2])
            else:
                comment = tuple_data[2]
            scan = tuple_data[3]
            time = tuple_data[4]
            new_list = (tile_name,tile,comment,scan,time)
            self.table_txt(new_list)
    # 定义一个存储信息的文件
    def table_txt(self,new_list):
        file_table = open('FJZ.txt','a+',encoding='utf-8')
        file_table.write('用户昵称:{}'.format(new_list[0]))
        file_table.write('\n')
        file_table.write('段子内容:{}'.format(new_list[1]))
        file_table.write('\n')
        file_table.write('段子评论:{}'.format(new_list[2]))
        file_table.write('\n')
        file_table.write('浏览量:{}'.format(new_list[3]))
        file_table.write('\n')
        file_table.write('时间:{}'.format(new_list[4]))
        file_table.write('\n')
        file_table.write('-----------请看下一个-----------')
        file_table.write('\n')

if __name__ == '__main__':
    spide = FJZDuanZi('duanzi')
    spide.all_page()

