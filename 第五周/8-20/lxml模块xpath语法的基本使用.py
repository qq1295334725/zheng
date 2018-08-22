"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:lxml模块xpath语法的基本使用.PY
@ide:PyCharm
@time:2018-08-20 15:31:48
"""
# lxml第三方的HTML解析库，在对html进行解析的时候，使用的是xpath语法，xpath全称是XML Path Language，也就是XML路径语言，它是一门在XML文档中查找信息的语言，它最初是搜寻XML文档的。但是它同样也适用于HTML的文档，xpath是通过路径表达式在HTML中选择节点。

# 导入lxml库中的etree模块，该模块可以自动修正HTML文本
from lxml import etree

# 创建一个ElementTree类型的对象
# 解析本地的html文件
html = etree.parse('index.html')
# 解析源码
# html_1=etree.HTML('网页源代码')
print(html)
print(type(html))
# tostring():将一个ElementTree对象转换成一个字符串
string = etree.tostring(html).decode('utf-8')
# print(string)
# print(type(string))
# fromstring():将一个字符串转换成ElementTree对象
string_test = '<a href="http://www.baidu.com">百度一下</a>'
element = etree.fromstring(string_test)
print(element)
print(type(element))


# 1.//表示从当前节点选择子孙节点
# //a:表示从根节点搜索所有的a标签，不考虑a标签的位置
a = html.xpath("//a")
print('======',a)
# 2./:表示从当前节点选择直接子节点
test = html.xpath("/html")
print(test)
# 获取li标签下面的a标签
a1 = html.xpath("//li/a")
print(a1)
# 获取ul标签的a标签
a2 = html.xpath("//ul/li/a")
print(a2)
a3 = html.xpath("//ul//a")
print(a3)
# 3.获取属性值,@class,@href,@stc,@id...
res = html.xpath("//a/@href")
print(res)
res = html.xpath("//a/@id")
print(res)
res = html.xpath("//a/@class")
print(res)
# 获取文本内容
# /text():只获取当前标签内的文本内容，而子孙标签的文本内容无法获取
res1 = html.xpath("//a/text()")
print(res1)
res3 = html.xpath("//p/text()")
print(res3)
res4 = html.xpath("//div/text()")
print(res4)
# //text():可以将该标签内及其所有子孙标签的文本内容全部获取出来
res5 = html.xpath("//div//text()")
print(res5)
# 5.通过属性值对要查找的标签进行限制
res6 = html.xpath("//a[@class='first_a']/text()")
print(res6)
res7 = html.xpath("//a[@id='second_a']/text()")
print(res7)
res8 = html.xpath('//p[@class="first second third"]/text()')
print(res8)
# [contains@(属性,"属性值")]：查找一个标签，并且该标签的某个属性包含xx。一般用于class属性(id也可以，但id是唯一的)
res9 = html.xpath('//p[contains(@class,"first")]/text()')
print(res9)
# 7.组合查询
res10 = html.xpath('//p[contains(@class,"second")and @id="one" ]/text()')
print(res10)

# 8.按序选择
# res11 = html.xpath("//li[last()]/a/text()")
res11 = html.xpath("//li[2]/a/text()")
print(res11)
res11 = html.xpath("//li[last()]/a[last()-1]/text()")
print(res11)


