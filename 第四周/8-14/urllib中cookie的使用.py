"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:urllib中cookie的使用.PY
@ide:PyCharm
@time:2018-08-14 11:08:04
"""
#----------------------------如何获取cookie信息--------------------------------------------
import http.cookiejar,urllib.request
#第一步声明一个Cookiejar对象
cookie_obj=http.cookiejar.CookieJar()
#第二步，根据cookiejar对象创建cookie信息的管理对象handler
handler=urllib.request.HTTPCookieProcessor(cookie_obj)
#第三步，根据handler对象创建一个opener对象
opener=urllib.request.build_opener(handler)
#第四步，根据opener对象打开网址
response=opener.open("http://www.baidu.com")
#这样CookieJar对象cookie_obj就保存了该网址的cookie信息
for item in cookie_obj:
    print(item.name+"=",item.value)

#----------------------如何将cookie信息保存到本地----------------------------
#                       cookieJar
#                            /
#                           FileCookieJar
#                          /          \
#                 MozillaCookieJar     LWPCookieJar
#
#MozillaCookieJar和LWPCookieJar都是用于将cookie信息保存为本地文件的一种形式，区别在于使用MozillaCookieJar生成的Cookie信息会保存为Mozilla类型的Cookie格式。使用LWPCookieJar会将cookie信息保存为libwww-perl格式的cookie文件。

#第一步：声明一个MozillaCookieJar或者LWPCookieJar的一个对象
cookie_mozilla_obj=http.cookiejar.MozillaCookieJar(filename="cookie.txt")
#第二步：根据MozlillaCookieJar生成的对象cookie_mozilla_obj，来创建一个cookie信息的管理对象handler
hanlder=urllib.request.HTTPCookieProcessor(cookie_mozilla_obj)
#第三步：根据handler对象创建opener对象
opener=urllib.request.build_opener(hanlder)
#第四步：根据opener对象对网址发起请求
response_test=opener.open("http://www.baidu.com")
#第五步：将cookie信息保存到本地
#ignore_descard=True。即使cookie信息在文件中已经存在，仍然对其进行覆盖写入。
#ignore_expires=True。即使cookie信息将要过期/作废，也要将其保存到文件
cookie_mozilla_obj.save(ignore_expires=True,ignore_discard=True)




#------------------------读取cookie信息对网站进行访问---------------------------
#第一步：声明一个MozillaCookieJar对象
cookie_obj=http.cookiejar.MozillaCookieJar()
#第二步：加载本地的cookie信息
#ignore_descard=True。即使cookie信息在文件中已经存在，仍然也要读取。
#igonre_expires=True。即使cookie信息将要过期/作废，也仍要读取cookie信息
cookie_obj.load(filename="cookie.txt",ignore_expires=True,ignore_discard=True)
#第三步：根据cookie_obj创建cookie信息的管理对象handler
handler=urllib.request.HTTPCookieProcessor(cookie_obj)
#第四步：根据handler创建一个opener对象
opener=urllib.request.build_opener(handler)
#第五步：根据opener对象调用open方法对网站发起请求
response_1=opener.open("http://www.baidu.com")
print(response_1.read().decode("utf-8"))



