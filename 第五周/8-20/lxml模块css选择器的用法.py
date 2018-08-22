"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:lxml模块css选择器的用法.PY
@ide:PyCharm
@time:2018-08-20 17:02:47
"""
from lxml import etree
# 解析本地文件用parse，解析源代码用HTML
# 选择器获取到的都是一个列表
html = etree.parse("index.html").getroot()
# html = etree.HTML("源代码")
# 使用标签选择器
title = html.cssselect("title")[0].text
print(title)
# 使用类选择器
a = html.cssselect(".first_a")[0].get("href")
print(a)
# 使用id选择器
a1 = html.cssselect("#second_a")[0].get("href")
print(a1)
# 使用属性选择器
a2 = html.cssselect("a[class='second_a']")[0].text
print(a2)
# 使用父子选择器
a3 = html.cssselect(".one>p")[0].text
print(a3)
# 使用后代选择器
a4 = html.cssselect(".one a")[0].text
print(a4)
# 使用交集选择器
a5 = html.cssselect("a.second_a")[0].text
print(a5)
# 使用伪类选择器
a6 = html.cssselect("li:nth-child(1)>a")[0].text
print(a6)










