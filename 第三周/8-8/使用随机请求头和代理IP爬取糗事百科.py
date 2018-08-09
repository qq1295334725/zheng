"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:使用随机请求头和代理IP爬取糗事百科.PY
@ide:PyCharm
@time:2018-08-08 09:26:51
"""
# 1.分析要爬取网站的URL，找到其中的规律
# 2.对网站发起请求，获取网页源代码
# 3.根据源代码，使用正则表达式匹配出来我们想要的信息。
# 4.把获取到的信息存储起来。
import urllib.request
from urllib.request import ProxyHandler,build_opener
import re
import random
import sqlite3
# 先设置要爬取网站的网址
base_url = 'https://www.qiushibaike.com/hot/'
# 设置一个请求头列表
user_agent_list = ['Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)','Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)']
# 设置一个代理IP
ip_list = [{'http':'http://111.155.116.234:8123'},{'http':'http://183.167.217.152:63000'},{'http':'http://110.73.9.193:8123'}]
# 设置请求头
headers = {
    'User-Agent':random.choice(user_agent_list)
}
# 设置IP代理对象
proxy_handler = ProxyHandler(random.choice(ip_list))
# 定义一个爬取糗事百科的函数
def download_qsbk(page):
    # 设置详细的url地址
    abs_url = base_url+"page/"+str(page)+"/"
    # 创建一个request对象
    request = urllib.request.Request(abs_url,headers=headers)
    # 根据IP代理对象设置opener对象
    opener = build_opener(proxy_handler)
    # 对网址发起访问，拿到源代码
    resoponse = opener.open(request).read().decode('utf-8')
    pattern_obj = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?class="articleGender .*?Icon">(.*?)</div>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats">.*?<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>',re.S)
    # pattern_obj = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?class="articleGender .*?Icon">(.*?)</div>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats">.*?<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>',re.S)
    # 定义一个去掉\n、<br/>、&quot:这个换行符的正则表达式
    remove_n = re.compile(r'\n')
    remove_br = re.compile(r'<br/>')
    remove_quote = re.compile(r'&quot:')
    all_info_list = re.findall(pattern_obj,resoponse)
    print(all_info_list)
    for nick_name,age,content,smile_num,comment_num in all_info_list:
        # 去掉昵称中的\n这个换行符
        nick_name = re.sub(remove_n,'',nick_name)
        # 去掉内容中的\n换行符
        content = re.sub(remove_n,'',content)
        # 去掉内容中的<br/>这个字符
        content = re.sub(remove_br,'',content)
        # 去掉内容中的&quot:这个字符
        content = re.sub(remove_quote,'',content)
        insert_sql = "insert into baike(nick_name,age,content,smile_num,comment_num)VALUES ('%s','%s','%s','%s','%s')"%(nick_name,age,content,smile_num,comment_num)
        cursor.execute(insert_sql)
        print('用户昵称:',nick_name)
        print('用户年龄:', age)
        print('内容:', content)
        print('好笑数:', smile_num)
        print('评论数:', comment_num)


if __name__ == '__main__':
    connect = sqlite3.connect('qsbk.db')
    cursor = connect.cursor()
    create_table = "create table baike(id INTEGER PRIMARY KEY,nick_name VARCHAR ,age VARCHAR ,content VARCHAR ,smile_num VARCHAR ,comment_num VARCHAR )"
    # cursor.execute(create_table)
    for x in range(1,10):
        download_qsbk(x)
    connect.commit()
    cursor.close()
    connect.close()

