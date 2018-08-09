"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:百度贴吧函数版爬虫.PY
@ide:PyCharm
@time:2018-08-08 16:04:12
"""
import urllib.request
from urllib.request import ProxyHandler,build_opener
import re
import random
#设置一个请求头列表
user_agent_list=['Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50','Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1','Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11']
#设置一个代理IP列表
ip_list=[{'http':'http://61.135.217.7:80'},{'http':'http://121.31.148.15:8123'},{'http':'http://1.194.122.221:8010'}]
#设置请求头
headers={
    'User-Agent':random.choice(user_agent_list)
}
#设置IP代理对象
proxy_handler=ProxyHandler(random.choice(ip_list))

#定义一个获取所有页码的函数
def get_total_page():
    request=urllib.request.Request(base_url,headers=headers)
    opener=build_opener(proxy_handler)
    try:
        response=opener.open(request)
    except Exception as e:
        print('链接失败的原因是：',e)
    else:
        html_string=response.read().decode('utf-8')
        pattern_obj=re.compile(r'<span class="red">(.*?)</span>',re.S)
        total_page=int(re.search(pattern_obj,html_string)[1])
        get_user_and_comment(total_page)
#定义一个爬取用户昵称和用户回复的函数
def get_user_and_comment(total_page):
    #先接收到get_total_page这个函数返回出来的总页码
    for page_num in range(1,total_page+1):
        print('正在爬取第{}页.....'.format(page_num))
        abs_url=base_url+'?pn='+str(page_num)
        request=urllib.request.Request(abs_url,headers=headers)
        opener=build_opener(proxy_handler)
        response=opener.open(request).read().decode('utf-8')
        pattern_obj=re.compile(r'<a.*?class="p_author_name.*?>(.*?)</a>.*?<div id="post_content.*?>(.*?)</div>',re.S)
        result_list=re.findall(pattern_obj,response)
        save_data(result_list)

#定一个去除不需要的数据并且保存数据的函数
def save_data(result_list):
    #先将get_user_and_comment里面的返回的result_list接收过来
    remove_n=re.compile(r'\n',re.S)
    remove_br=re.compile(r'<br>',re.S)
    remove_img=re.compile(r'(.*?)<img',re.S)
    file_test=open('{}.txt'.format(tie_zi_id),'a+',encoding='utf-8')
    for tuple_data in result_list:
        #从tuple_data这个元组中的第0个元素也就是昵称中，去除img以及后面的内容，只保留昵称
        if 'img' in tuple_data[0]:
            nick_name=re.search(remove_img,tuple_data[0])[1]
        else:
            nick_name=tuple_data[0]
        #从tuple_data这个元组中的第1个元素也就是评论内容中，去除\n这个换行符。
        if 'img' in tuple_data[1]:
            content=re.search(remove_img,tuple_data[1])[1]
            content = re.sub(remove_n, '', content)
            # 从已经去除过换行符的content中继续去除<br>这个字符
            content = re.sub(remove_br, '', content)
        else:
            content=tuple_data[1]
            content = re.sub(remove_n, '', content)
            # 从已经去除过换行符的content中继续去除<br>这个字符
            content = re.sub(remove_br, '', content)
        file_test.write('用户昵称：{}'.format(nick_name))
        file_test.write('\n')
        file_test.write('用户回复：{}'.format(content))
        file_test.write('\n')
    file_test.close()
    print('数据写入成功！')



if __name__ == '__main__':
    tie_zi_id=input('请输入你要爬取的帖子的ID:')
    base_url="https://tieba.baidu.com/p/{}".format(tie_zi_id)
    get_total_page()
     # 5823687933
    baser_url = "https://tieba.baidu.com/p/{}".format(tie_zi_id)
    get_total_page()





