"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:1111.PY
@ide:PyCharm
@time:2018-08-08 19:02:44
"""
import sqlite3
import re
import random
import urllib.request
from urllib.request import ProxyHandler,build_opener
user_agent = ['Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1;Maxthon 2.0)',' Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1;360SE)']
ip_list = [{'http':'http://180.118.243.224:808'},{'http':'http://119.5.0.33:808'}]
url_base = 'https://www.qiushibaike.com/hot/'
headers = {'User-Agent':random.choice(user_agent)}
proxy_handler = ProxyHandler(random.choice(ip_list))

def QSBK_url(page_all):
    new_url_base = url_base+'page/'+str(page_all)+'/'
    request = urllib.request.Request(new_url_base,headers=headers)
    opener = build_opener(proxy_handler)
    request = opener.open(request)
    response = request.read().decode('utf-8')

    pattern_obj = re.compile(
        r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?class="articleGender .*?Icon">(.*?)</div>.*?<div class="content">.*?<span>(.*?)</span>.*?<div class="stats">.*?<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>',
        re.S)
    remove_n = re.compile(r'\n')
    remove_br = re.compile(r'<br/>')
    remove_quote = re.compile(r'&quot:')
    all_info_list = re.findall(pattern_obj,response)
    for nick_name, age, content, smile_num, comment_num in all_info_list:
        nick_name = re.sub(remove_n,'',nick_name)
        content = re.sub(remove_n,'',content)
        content = re.sub(remove_br,'',content)
        content = re.sub(remove_quote,'',content)
        insert_into = "insert into base(nick_name, age, content, smile_num, comment_num)VALUES ('%s','%s','%s','%s','%s')"%(nick_name, age, content, smile_num, comment_num)
        cursor.execute(insert_into)



if __name__ == '__main__':
    connect = sqlite3.connect('XSBK.db')
    cursor = connect.cursor()
    create_table = "create table if not EXISTS base(ip INTEGER PRIMARY KEY ,nick_name VARCHAR ,age VARCHAR ,content VARCHAR ,smile_num VARCHAR ,comment_num VARCHAR )"
    for x in range(1,11):
        QSBK_url(x)
    cursor.execute(create_table)
    connect.commit()
    cursor.close()
    connect.close()

























