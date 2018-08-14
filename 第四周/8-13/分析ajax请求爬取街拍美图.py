"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:分析ajax请求爬取街拍美图.PY
@ide:PyCharm
@time:2018-08-13 15:01:04
"""
import urllib.request
from urllib.parse import urlencode
import json
import os
import random
from urllib.request import ProxyHandler,build_opener
class JPMTSpider(object):
    user_agent_list = [
        'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
        'Mozilla/5.0Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
        'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11']
    # 设置一个代理IP
    ip_list = [{'http': 'http://111.155.116.235	:8123'}, {'http': 'http://61.135.217.7:80'},
               {'http': 'http://110.73.9.193:8123'}, {'https': 'https://101.132.122.230:3128'}]
    def __init__(self,offset,keyword):
        self.headers = {'User-Agent':random.choice(self.user_agent_list)}
        self.ip = random.choice(self.ip_list)
        self.base_url = "https://www.toutiao.com/search_content/?"
        self.offset = offset
        self.keyword = keyword
    def get_page(self):
        # 构造get请求的参数
        params = {
            "offset":self.offset,
            "format":"json",
            "keyword":self.keyword,
            "autoload":"true",
            "count":20,
            "cur_tab":1,
            "from":"search_tab"
        }
        url = self.base_url+urlencode(params)
        request=urllib.request.Request(url,headers=self.headers)
        ip_proxyhandler = ProxyHandler(self.ip)
        opener = build_opener(ip_proxyhandler)
        urllib.request.install_opener(opener)
        try:
            response = urllib.request.urlopen(request)
            if response.status==200:
                # 拿到的源代码是json数据
                html = response.read().decode('utf-8')
                # 调用parse_json来解析json数据
                self.parse_json(html)
        except Exception as e:
            return None
    # 定义一个函数来解析json
    def parse_json(self,html):
        # 由于获得的网页源代码是字符串，所有需要调用loads方法进行反序列化，得到的是一个字典
        json_data = json.loads(html)
        # 先判断json_data这个字典当中有没有data这个键
        if json_data.get('data'):
            # 如果有data这个键，则将data这个键对应的列表取出来
            # 遍历json_data对应的列表，每一个item对应的都是一个字典
            for item in json_data.get('data'):
                # 将item这个字典里面的键img_list取出来，对应的结果就是一个列表
                image_list=item.get("image_list")
                # 将item这个字典里面的键title对应的值取出来
                title=item.get("title")
                self.save_image(title,image_list)


    def save_image(self,title,image_list):
        # 先判断是否存在title这个文件夹
        if not os.path.exists(title):
            # 如果没有title这个文件夹再创建
            os.mkdir(title)
        # 先遍历image_list，image_list对应的是一个列表，每一个url_data是一个字典
        for url_dict in image_list:
            # 从url_dict这个字典中获取url这个键对应的值是图片的地址
            url = url_dict.get("url")
            # 拼接出来图片的完整地址
            image_url = "http:"+url
            # 给图片设置名称
            img_name = url.split('/')[-1]
            try:
                response=urllib.request.urlopen(image_url)
                if response.status==200:
                    # 给每一张图片拼接一个完整的路径
                    file_path='{0}/{1}.{2}'.format(title,img_name,'jpg')
                    # 判断title这个文件夹当中有没有img_name这个图片
                    if not os.path.exists(file_path):
                        # with open上下文管理器，使用它不需要手动关闭文件
                        with open(file_path,'wb') as f:
                            # response.read()拿到的数据本身就是图片的二进制数据，所以不需要decode转换编码，因为存储图片的时候存储的就是二进制数据
                            f.write(response.read())
                    else:
                        print('该图片已经存在')
            except Exception as e:
                print('保存图片失败，原因是：',e)

if __name__ == '__main__':
    for x in range(0,100,20):
        spider = JPMTSpider(x,"街拍美图")
        spider.get_page()



