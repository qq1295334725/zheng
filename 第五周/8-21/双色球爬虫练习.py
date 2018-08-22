"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:双色球爬虫练习.PY
@ide:PyCharm
@time:2018-08-21 19:22:37
"""
import requests
from fake_useragent import UserAgent
from tqdm import tqdm
import xlwt
import csv
from lxml import etree

class SSQ(object):
    def __init__(self):
        self.base_url = 'http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp'
        self.headers={
            'User-Agent':UserAgent().random
        }
        self.big_list = []

    def get_page_num(self):
        '''
        获取网页的页数
        :return:
        '''
        # url = self.base_url+self.type+'/'+self.page_table+'/#'
        # url = 'http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp'
        response = requests.get(self.base_url, headers=self.headers).content.decode('utf-8')
        html = etree.HTML(response)
        total_page_num=int(html.xpath("//p[@class='pg']/strong[1]/text()")[0])
        self.get_total(total_page_num)


    def get_total(self,total_page_num):
        '''
        获取网页的源代码
        :return:
        '''
        for page_num in tqdm(range(1,total_page_num+1)):
            # print('正在爬取第{}页,请稍等...'.format(page_num))
            url = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_'+str(page_num)+'.html'
            response=requests.get(url, headers=self.headers).text
            # print(response)
            html=etree.HTML(response)
            data_1_list=html.xpath('//table[@class="wqhgt"]//tr/td[@align="center"][1]/text()')#-1
            data_list = data_1_list[0:len(data_1_list)-1]
            issue_list = html.xpath('//table[@class="wqhgt"]//tr/td[@align="center"][2]//text()')
            winning_list_1 = html.xpath('//table[@class="wqhgt"]//tr//em//text()')
            winning_list=[]
            y=0
            while y+7<=len(winning_list_1):
                winning_list_2=winning_list_1[y:y+7]
                y += 7
                winning_list.append(winning_list_2)
            sale_1_list = html.xpath('//table[@class="wqhgt"]//tr//td[4]//strong//text()')#21号没数据
            one_list = html.xpath('//table[@class="wqhgt"]//tr//td[5]//strong//text()')
            two_list = html.xpath('//table[@class="wqhgt"]//tr//td[6]//strong//text()')
            for x in range(0,len(data_list)):
                big_dict={"开奖日期":data_list[x],"期号":issue_list[x],"中奖号码":winning_list[x],"销售额":sale_1_list[x],"一等奖":one_list[x],"二等奖":two_list[x]}
                self.big_list.append(big_dict)

    def write_data(self):
        with open("双色球.csv", 'w', encoding='utf-8', newline="")as f:
            writer = csv.DictWriter(f,fieldnames=["开奖日期","期号","中奖号码","销售额","一等奖","二等奖"])
            writer.writeheader()
            writer.writerows(self.big_list)

    def start_spider(self):
        self.get_page_num()
        self.write_data()


if __name__ == '__main__':
    s = SSQ()
    s.start_spider()





























