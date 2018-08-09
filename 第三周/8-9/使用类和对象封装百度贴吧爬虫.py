"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用类和对象封装百度贴吧爬虫.PY
@ide:PyCharm
@time:2018-08-09 09:18:16
"""
import urllib.request
import re
import random
from urllib.request import ProxyHandler,build_opener
class BDTBSpider(object):
    # 设置一个请求头列表
    user_agent_list = [
        'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
        'Mozilla/5.0Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
        'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11']
    # 设置一个代理IP列表
    ip_list = [{'http': 'http://61.135.217.7:80'}, {'http': 'http://121.31.148.15:8123'},
               {'http': 'http://1.194.122.221:8010'}]

    def __init__(self,tie_ba_id):
        #tie_ba_id是创建对象的时候，传递过来的值，然后赋值给了self.tie_ba_id这个属性
        self.tie_ba_id=tie_ba_id
        #再将tie_ba_id这个值和https://tieba.baidu.com/p/{}进行拼接就得到了贴子的完整链接
        self.base_url="https://tieba.baidu.com/p/{}".format(self.tie_ba_id)
        #设置请求头,从user_agent_list这个列表中随机选取一个浏览器标识，用来设置请求头
        self.headers={'User-Agent':random.choice(self.user_agent_list)}
        #设置ip,从ip_list这个列表当中随机选择一个ip，接着根据这个ip创建ip代理对象
        self.ip=random.choice(self.ip_list)

    #定义一个获取总页数的函数，目的是为了能自动爬取所有页数的数据。
    def get_total_page(self):
        #创建request对象
        request=urllib.request.Request(url=self.base_url,headers=self.headers)
        #创建IP代理对象
        ip_proxyhandler=ProxyHandler(self.ip)
        #创建opener
        opener=build_opener(ip_proxyhandler)
        #根据opener对象调用open方法对网页发起请求，拿到源代码
        response=opener.open(request).read().decode('utf-8')
        #创建正则表达式匹配规则
        patter_obj=re.compile(r'<span class="red">(.*?)</span>',re.S)
        #通过调用re.search这个函数从源代码中提取总页数
        #由于拿到的total_page是字符串，所有要使用int转换成整数
        total_page=int(re.search(patter_obj,response)[1])
        #在get_total_page这个函数中，调用get_user_and_comment这个函数，并且把get_total_page中的total_page当做实参传递给
        #get_user_and_comment这个函数中的形参,这个时候total_page_1这个形参就接收到total_page这个实参的值。
        self.get_user_and_comment(total_page)

    #定义一个获取详细信息的函数
    #定义一个形参，接收get_total_page函数中的total_page，目的是为了在get_user_and_comment函数中接收total_page来进行使用
    def get_user_and_comment(self,total_page_1):
        #遍历所有页，拿到每一页的页码。page_num指的就是每一页的页码
        for page_num in range(1,total_page_1+1):
           print('正在爬取第{}页,请稍后.....'.format(page_num))
           #拼接完整的url,让网址变成每一页的完整网址
           abs_url=self.base_url+"?pn="+str(page_num)
           request=urllib.request.Request(url=abs_url,headers=self.headers)
           ip_proxy_handler=ProxyHandler(self.ip)
           opener=build_opener(ip_proxy_handler)
           response=opener.open(request).read().decode('utf-8')
           #定义正则表达式规则，从每一页中提取想要的数据信息
           pattern_obj = re.compile(r'<a.*?class="p_author_name.*?>(.*?)</a>.*?<div id="post_content.*?>(.*?)</div>',re.S)
           #使用findall匹配到每一页中的所有需要的数据，返回值是一个列表，里面套着元组，一个元组对应着一个用户的昵称还有回复信息。
           result_list=re.findall(pattern_obj,response)
           #将匹配到的result_list的数据，放置到update_data这个函数中进行处理
           self.update_data(result_list)
    #定义一个函数来处理匹配到的数据
    def update_data(self,result_list):
        remove_n = re.compile(r'\n', re.S)
        remove_br = re.compile(r'<br>', re.S)
        remove_img = re.compile(r'(.*?)<img', re.S)
        remove_space=re.compile(r' ',re.S)
        #遍历result_list，每一个tuple_data对应着一个元组信息，每一个元组存放着用户昵称和用户回复信息
        for tuple_data in result_list:
            #先判断用户昵称中是否含有img,如果有进行相应的清理数据的工作
            if "img" in tuple_data[0]:
                #如果昵称中含有img这个字符串，则通过search将昵称匹配出来，去除掉后面跟着的img
                nick_name=re.search(remove_img,tuple_data[0])[1]
            else:
                #如果名字中不包含img这个字符串，则说明是一个正常的昵称，不需要做处理
                nick_name=tuple_data[0]
            nick_name=re.sub(remove_space,'',nick_name)
            #先判断用户回复中是否含有img，如果有进行相应的清理数据的工作
            if "img" in tuple_data[1]:
                # 如果用户回复中含有img这个字符串，则通过search将昵称匹配出来，去除掉后面跟着的img
                content=re.search(remove_img,tuple_data[1])[1]
            else:
                # 如果回复中不包含img这个字符串，则说明是一个正常的昵称，不需要做处理
                content=tuple_data[1]
            #将content里面的\n这个换行符去除掉，替换成空
            new_content=re.sub(remove_n,'',content)
            #将已经去除过\n的new_content继续使用re.sub去除里面的br，得到的新数据赋值给new_content
            new_content=re.sub(remove_br,'',new_content)
            #再将nick_name和new_content放置到元组中进行返回
            new_content=re.sub(remove_space,'',new_content)
            new_tuple=(nick_name,new_content)
            #将new_tuple这个实参传入到save_data的形参当中，供save_data这个函数使用
            self.save_data(new_tuple)

    #定义一个函数来存储数据
    def save_data(self,new_tuple):
        #接收到new_tuple进行数据的存储
        #使用self.tie_ba_id对文件进行命名
        #由于save_data是在update_data这个函数的for循环中调用的，所有一旦使用w模式打开文件就会不断覆盖前一页的内容，所有使用a+这样追加写入的模式
        file_test=open("{}.txt".format(self.tie_ba_id),'a+',encoding='utf-8')
        file_test.write("用户昵称:{}".format(new_tuple[0]))
        file_test.write("\n")
        file_test.write("用户回复:{}".format(new_tuple[1]))
        file_test.write("\n")
        file_test.write("--------------------------------")
        file_test.write("\n")

    #设置一个爬取的启动函数
    def start_spider(self):
        print('百度贴吧爬虫已启动！')
        self.get_total_page()


if __name__ == '__main__':
    Spider=BDTBSpider('5831574532')
    Spider.start_spider()



