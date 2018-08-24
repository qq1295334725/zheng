"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:11.PY
@ide:PyCharm
@time:2018-08-22 17:47:01
"""
import requests
from fake_useragent import UserAgent
from lxml import etree
import pymongo
from tqdm import tqdm


class Music(object):
    def __init__(self):
        self.base_url = 'http://www.kuwo.cn/bang/index'
        self.headers = {
            'User-Agent': UserAgent().random
        }

    def get_total(self):
        retry_link_count = 0
        while True:
            try:
                response = requests.get(self.base_url, headers=self.headers).text
            except Exception as e:
                print('连接音乐网失败，原因是：', e)
                print("正在尝试第{}次重连……".format(retry_link_count))
                retry_link_count += 1
                if retry_link_count >= 5:
                    print("尝试连接次数已经达到五次，停止连接")
                    break
            else:
                html = etree.HTML(response)
                return html

    def get_num(self):
        html = self.get_total()
        html_obj = html.cssselect('.listMusic>li')
        # print(type(html_obj))
        for li in html_obj:
            # print(li.div.p.get("class"))
            music_num = html.cssselect('.listMusic>li>div:nth-child(1)>p')[0].text
            music_name = html.cssselect('.listMusic>li>div:nth-child(2)>a')[0].text
            author_name = html.cssselect('.listMusic>li:nth-child(2)>div:nth-child(3)>a')[0].text
            print(music_name)


        # for x in tqdm(range(0, len(html_obj))):
        #     dict_music = {"音乐": music_name[x], "作者": author_name[x], "排名": rank_num[x]}
        #     collection.insert_one(dict_music)


if __name__ == '__main__':
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client.novel
    collection = db.music
    s = Music()
    s.get_num()
