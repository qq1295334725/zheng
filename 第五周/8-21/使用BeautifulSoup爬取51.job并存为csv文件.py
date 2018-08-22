"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用BeautifulSoup爬取51.job并存为csv文件.PY
@ide:PyCharm
@time:2018-08-21 15:48:28
"""
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
import re
import csv

class Job51Spider(object):
    def __init__(self,city_num,work_name,page_num):
        self.city_num = city_num
        self.work_name = work_name
        self.page_num = page_num
        self.base_url = 'https://search.51job.com/list/{},000000,0000,00,9,99,{},2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(self.city_num, self.work_name, self.page_num)
        self.headers = {
            'User-Agent':UserAgent().random
        }
        self.big_list=[]

    def get_total_page_num(self):
        '''
        获取总页码
        :return:
        '''
        response = requests.get(self.base_url, headers=self.headers)
        response.encoding="gb18030"
        pattern = re.compile(r'<span class="td">共(.*?)页',re.S)
        total_page_num = re.search(pattern, response.text)[1]
        self.get_page_code(total_page_num)


    def get_page_code(self,total_page_num):
        for page_num in tqdm(range(1,int(total_page_num)+1)):
            every_page_url = 'https://search.51job.com/list/{},000000,0000,00,9,99,{},2,{}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(self.city_num, self.work_name, page_num)
            response = requests.get(every_page_url,headers=self.headers)
            response.encoding="gb18030"
            bs = BeautifulSoup(response.text,'lxml')
            div_list=bs.select("#resultList .el")
            del div_list[0]
            # 遍历div_list这个列表，取出每个div标签
            for div in div_list:
                job_name=div.select(".t1 a")[0]["title"]
                company_name=div.select(".t2 a")[0]["title"]
                work_name=div.select(".t3")[0].string
                salary=div.select(".t4")[0].string
                date=div.select(".t5")[0].string
                dict_job={"工作名称":job_name,"公司名称":company_name,"工作地点":work_name,"工作薪资":salary,"发布时间":date}
                self.big_list.append(dict_job)


    def write_date(self):
        with open("%s+%s.csv"%(self.city_num,self.work_name),'w',encoding='utf-8',newline='')as f:
            # 创建一个用于写入字典数据的对象
            writer=csv.DictWriter(f,fieldnames=["工作名称","公司名称","工作地点","工作薪资","发布时间"])
            # 将表头写入
            writer.writeheader()
            writer.writerows(self.big_list)

    def start_spider(self):
        self.get_total_page_num()
        self.write_date()


if __name__ == '__main__':
    spider = Job51Spider('170200','python','1')
    spider.start_spider()



