"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用BS4爬取天堂图片网图片.PY
@ide:PyCharm
@time:2018-08-17 09:58:59
"""
import os
import requests
from bs4 import BeautifulSoup
import shutil
from urllib.request import urlretrieve
# urlretrieve下载图片

# 定义一个图片爬虫类
class TianTangSpider(object):
    def __init__(self):
        self.base_url = "http://www.ivsky.com"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0"
        }
        self.current_page_num = 1


    def get_page_code(self, url):
        '''
        定义一个获取网页源代码的函数
        :param url: 网址的部分路径/tupian/index_1.html
        :return: 没有返回值
        '''
        # 拼接每一页的完整路径
        abs_url = self.base_url+url
        try:
            response = requests.get(abs_url, headers=self.headers).text
        except Exception as e:
            print('链接失败，原因是：',e)
        else:
            self.get_images_by_html(response)

    def get_images_by_html(self, page_code):
        '''
        根据每一页的页面源代码，获取网页中每一个小分类的名称，每一个小分类的地址
        :param page_code:每一页的页面源代码
        :return: 无返回值
        '''
        print('正在下载第{}页图片......'.format(self.current_page_num))
        # 创建一个文档树对象
        bs_soup = BeautifulSoup(page_code,"lxml")
        # .il_img获取的是class属性值是il_img的标签，a匹配的是这个标签下面a的标签
        a_list = bs_soup.select(".il_img a")
        # 给每一页的图片单独创建一个文件夹，用于存放该页的图片
        page_num = "第%d页图片"%self.current_page_num
        os.mkdir(page_num)
        os.chdir(page_num)
        # 遍历a标签的列表，取出每一个a标签
        for a in a_list:
            # 取出a标签的href属性
            a_href = a["href"]
            a_title = a["title"]
            # 以a标签的title属性的值作为每个小分类的文件夹的名称
            # 判断文件夹是否存在，
            if os.path.exists(a_title):
                # 递归的去删除文件
                shutil.rmtree(a_title)
            os.mkdir(a_title)
            os.chdir(a_title)
            self.download_detail_imgs(a_href)
            # 在这个地方调用下载图片的函数下载到对应的小分类文件夹当中
            # 当每一个小分类的图片下载完成之后，需要切换到第几页图片这层目录当中，接着在第几页图片这层目录当中在创建小分类文件夹
            os.chdir(os.path.pardir)
        # 回到imgs这层文件夹，再接着创建下一页图片的文件夹
        os.chdir(os.path.pardir)
        self.current_page_num += 1
        # 调用获取下一页地址的函数
        self.get_next_url(bs_soup)



    def download_detail_imgs(self, url):
        '''
        下载图片
        :param url: 图片详情页地址的部分路径
        :return:
        '''
        abs_url = self.base_url+url
        response = requests.get(abs_url, headers=self.headers).text
        # print(response)
        bs_soup = BeautifulSoup(response,"lxml")
        img_list = bs_soup.select(".il_img a img")
        # 遍历img标签的列表，取出每一个img标签
        for img in img_list:
            # 取出每一张图片的地址
            src = img.get("src")
            # 给每一张图片设置一个名字
            img_name = src.split("/")[-1]
            # 下载图片的时候要加上后缀(.jpg),img_name有后缀.jpg所以不需要加了
            urlretrieve(src,img_name)

    def get_next_url(self, bs_soup):
        '''
        将每一页的源代码的bs对象传过来，用于解析每一页中 下一页的地址的部分路径
        :param bs_soup:每一页源代码的bs对象
        :return:
        '''
        a_list = bs_soup.select(".page-next")
        if len(a_list)==0:
            print('所有页的图片已经下载完毕，没有下一页')
        else:
            a = a_list[0]
            next_page_url = a.get("href")
            # 获取下一页的源代码
            self.get_page_code(next_page_url)

    def start_spider(self):
        '''
        启动函数
        :return:
        '''
        if os.path.exists("images"):
            shutil.rmtree("images")
        os.mkdir("images")
        os.chdir("images")
        self.get_page_code("/tupian/index_1.html")

if __name__ == '__main__':
    spider = TianTangSpider()
    spider.start_spider()



