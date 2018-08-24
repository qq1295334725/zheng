"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用lxml的xpath语法爬取豆瓣电影Top250.PY
@ide:PyCharm
@time:2018-08-23 11:00:15
"""
import requests
from lxml import etree
from fake_useragent import UserAgent
import csv
class DouBanMovie(object):
    def __init__(self):
        self.headers = {
            "User-Agent":UserAgent().random
        }
        self.base_url = 'https://movie.douban.com/top250'

    def get_page_code(self):
        for x in range(0,250,25):
            abs_url = self.base_url+'?start={}&filter='.format(x)
            print('正在爬取链接为{}的页面源代码……'.format(abs_url))
            response = requests.get(abs_url,headers=self.headers).text
            self.parse_html(response)

    def parse_html(self, response):
        html_obj = etree.HTML(response)
        div_list = html_obj.xpath("//ol/li/div")
        for div in div_list:
            rank = div.xpath("div[1]/em/text()")
            #span标签里的所有的文本都是名字（）
            movie_name = div.xpath("div[2]/div[1]//span/text()")
            director = div.xpath("div[2]/div[2]/p[1]/text()")
            grade = div.xpath("div[2]/div[2]/div/span[2]/text()")
            comment_num = div.xpath("div[2]/div[2]/div/span[4]/text()")
            short_comment = div.xpath("div[2]/div[2]/p/span/text()")

            movie_string = ""
            for movie in movie_name:
                movie_string += movie

            movie_director_string = ""
            for movie_1 in director:
                movie_1 = movie_1.replace("\n", "")
                movie_1 = movie_1.replace(" ", "")
                movie_director_string += movie_1
            dict_info = {"电影排名":rank, "电影名称":movie_name, "演员表":director, "电影评分":grade, "电影评论数":comment_num, "电影短评":short_comment}
            # self.clear_data(dict_info)

    def write_csv(self):
        with open("movie.csv", "w",encoding='utf-8',newline="") as csv_file:
            writer = csv.DictWriter(csv_file,fieldnames=["电影排名","电影名称","演员表",'电影评分',"电影评论数","电影短评"])
            writer.writeheader()





























