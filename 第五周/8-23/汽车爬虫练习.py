"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:汽车爬虫练习.PY
@ide:PyCharm
@time:2018-08-23 17:50:32
"""
import requests
from fake_useragent import UserAgent
from lxml import etree
import csv
import zmail
class KPLScore(object):
    def __init__(self):
        self.base_url = 'https://top.16888.com/auto_rqjb2_'
        self.headers = {
            "User-Agent":UserAgent().random
        }
        self.big_list=[]

    def page_num(self):
        url = 'https://top.16888.com/auto_rqjb2.html'
        response = requests.get(url, headers=self.headers).text

        html = etree.HTML(response)
        # for x in range(0,5):
        page_number = html.xpath("//div[@class='table_show']//div/a[4]/text()")[0]
        return page_number



    def get_table(self):
        # url = self.base_url+url_little
        page = int(self.page_num())
        for page_num in range(1,page):
            url = self.base_url+str(page_num)+'.html'
            response = requests.get(url, headers=self.headers).text
            html = etree.HTML(response)
            li_list = html.xpath("//div[@class='table_show']//table/tr")
            # print(len(li_list))
            # print(li_list)
            for tr in range(1,len(li_list)):
                car_type = li_list[tr].xpath("td[1]/em/text()")[0]
                # print(car_type)
                car_name = li_list[tr].xpath("td[2]/a/text()")[0]
                car_cost = li_list[tr].xpath("td[3]/a/text()")
                if car_cost==[]:
                    car_cost=''
                else:
                    car_cost=car_cost[0]
                car_att = li_list[tr].xpath("td[4]/text()")[0]
                car_grade = li_list[tr].xpath("td[5]/a/text()")[0]
                car_oil = li_list[tr].xpath("td[6]/a/text()")[0]
                dict_job = {"汽车类型": car_type, "汽车名字": car_name, "售价": car_cost, "关注度":car_att,"评分":car_grade,"油耗": car_oil}
                self.big_list.append(dict_job)


    def write_data(self):
        with open("car.csv", "a+", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["汽车类型", "汽车名字", "售价","关注度","评分","油耗"])
            writer.writeheader()
            writer.writerows(self.big_list)

    def send_mail(self):
        mail_content={
            "subject":"陈鹏",
            "content":"https://top.16888.com/auto_rqjb2.html",
            "attachments":["car.csv"]
        }



    def start_spider(self):
        self.get_table()
        self.write_data()
if __name__ == '__main__':
    s = KPLScore()
    s.start_spider()



