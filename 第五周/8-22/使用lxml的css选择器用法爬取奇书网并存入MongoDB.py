"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用lxml的css选择器用法爬取奇书网并存入MongoDB.PY
@ide:PyCharm
@time:2018-08-22 15:34:03
"""
import requests
from lxml import etree
from fake_useragent import UserAgent
import pymongo
class QiShuSpider(object):
    def __init__(self):
        self.base_url = 'https://www.qisuu.la/soft/sort01/'
        self.headers = {
            'User-Agent':UserAgent().random,
            "HOST":"www.qisuu.la",
            "Referer":"https://www.qisuu.la"
        }

    def get_index_code(self):
        # 声明一个变量，来记录重连的次数
        retry_link_count=0
        while True:
            try:
                response = requests.get(self.base_url, headers = self.headers)
            except Exception as e:
                print('连接奇书网失败，原因是：',e)
                print("正在尝试第{}次重连……".format(retry_link_count))
                retry_link_count += 1
                if retry_link_count>=5:
                    print("尝试连接次数已经达到五次，停止连接")
                    break
            else:
                html_obj = etree.HTML(response.text)
                # 获取option这个标签的列表
                option_list = html_obj.cssselect('select>option')
                # for option in page_url_list:
                # every_page_url = option.get("value")
                # print(every_page_url)
                return option_list

    def get_every_page_code(self):
        option_list = self.get_index_code()
        for option in option_list:
            value = option.get("value")
            # 拼接每一页的完整地址
            base_url = "https://www.qisuu.la"+value
            print('正在爬取{}连接……'.format(base_url))
            response = requests.get(base_url, headers=self.headers).text
            html_obj = etree.HTML(response)
            # 获取每一本小说所在a标签的一个列表
            a_list = html_obj.cssselect(".listBox li>a")
            for a in a_list:
                nover_href = a.get("href")
                # 拼接每一本小说的完整地址
                nover_url = "https://www.qisuu.la"+nover_href
                self.parse_every_novel(nover_url)

    def parse_every_novel(self, novel_url):
        response = requests.get(novel_url,headers=self.headers)
        response.encoding='utf-8'
        html_obj = etree.HTML(response.text)
        # print(html_obj)
        nove_name = html_obj.cssselect(".detail_right>h1")[0].text
        # print(nove_name)
        clik_num = html_obj.cssselect(".detail_right>ul>li:nth-child(1)")[0].text
        novel_num = html_obj.cssselect(".detail_right>ul>li:nth-child(2)")[0].text
        novel_type = html_obj.cssselect(".detail_right>ul>li:nth-child(3)")[0].text
        update_time = html_obj.cssselect(".detail_right>ul>li:nth-child(4)")[0].text
        novel_status = html_obj.cssselect(".detail_right>ul>li:nth-child(5)")[0].text
        novel_author = html_obj.cssselect(".detail_right>ul>li:nth-child(6)")[0].text
        novel_run_envir = html_obj.cssselect(".detail_right>ul>li:nth-child(7)")[0].text
        novel_latest_chapter = html_obj.cssselect(".detail_right>ul>li:nth-child(8)>a")[0].text
        dict_novel = {"小说名称":nove_name, "点击次数":clik_num, "小说大小":novel_num, "小说类型":novel_type, "更新时间":update_time, "小说状态":novel_status, "小说作者":novel_author, "小说运行环境":novel_run_envir, "小说最新章节":novel_latest_chapter}
        collection.insert_one(dict_novel)




    def start_mongodb(self):
        self.get_every_page_code()


if __name__ == '__main__':
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client.novel
    collection = db.novel

    qishu = QiShuSpider()
    qishu.start_mongodb()


