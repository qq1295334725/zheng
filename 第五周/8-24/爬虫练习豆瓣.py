"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:爬虫练习豆瓣.PY
@ide:PyCharm
@time:2018-08-24 11:05:57
"""
import requests
from tqdm import tqdm
from lxml import etree
import csv
from fake_useragent import UserAgent
import re
class DouBanYingPing(object):
    def __init__(self):
        self.base_url = 'https://movie.douban.com/top250'
        self.headers = {
            'User-Agent':UserAgent().random
        }


    # 获取总的电影数
    def page_total_num(self):
        response = requests.get(self.base_url, headers=self.headers).text
        pattern = re.compile(r'<span class="count">.*?共(.*?)条',re.S)
        movie_num = int(re.search(pattern, response)[1])
        # print(movie_num)
        self.get_many_movie_comment(movie_num)

    # 获取电影链接
    def get_many_movie_comment(self,movie_num):
        for page in range(0,movie_num,25):
            url = self.base_url+'?start={}'.format(page)+'&filter='
            response = requests.get(url, headers=self.headers).text
            # print(response)
            html_obj = etree.HTML(response)
            li_list = html_obj.xpath('//ol[@class="grid_view"]')
            # print(li_list)
            for li in li_list:
                movie_url = li.xpath('li/div/div[1]/a/@href')
                print(movie_url)






if __name__ == '__main__':
    s = DouBanYingPing()

    # s.response_movie()
    s.page_total_num()





















