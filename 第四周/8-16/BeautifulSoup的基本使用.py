"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:BeautifulSoup的基本使用.PY
@ide:PyCharm
@time:2018-08-16 15:05:29
"""

# BeautifulSoup是python支持的第三方库。它的主要作用是可以非常方便的从HTML网页中提取所需要的数据。
# lxml是一个第三方的解析库，默认情况写BS4会使用python自带的解析器去解析html页面，但是lxml解析速度更快，功能上更为强大，因为它的底层是通过c语言实现的。
import re
from bs4 import BeautifulSoup
# 创建一个BeautifulSoup对象
bs = BeautifulSoup(open("index.html",encoding='utf-8'),"lxml")
# BeautifulSoup()类，它是一个HTML文档，转换成一个复杂的，有层次的树形结构，从而形成父节点和子节点之间的关系，每一个节点对应一个特殊对象。
# 树形结构中的Python对象类型：
# BeautifulSoup：一般指代的是整个html文档
# Tag：指代的就是html文档中的一个标签，有两个重要的属性，name，attrs
# NavigableString：指代的就是标签中的文字。
# Comment：这个对象是一个特殊的NavigableString对象，其输出的内容是注释但是不包含注释符号。
# print(bs)
#
# # # --------------选择元素--------------
# # # 获取HTML文档中title标签的内容
# print(bs.title)
# print(type(bs.title))
# #
# # # 获取html文当中a标签的内容(会匹配第一个符合要求的a标签）
# print(bs.a)
# print(type(bs.a))
# # # 获取html文档中的div标签的内容
# print(bs.div)
# print(type(bs.div))
# # # 获取html文档中div下面的a标签的内容
# print(bs.div.a)

#
# ---------提取信息（标签名称，属性值，文本）----
# 获取标签的名称，name属性是在获取当前标签的名称
# print(bs.head.name)
# print(bs.title.name)
# print(bs.title.attrs)
# # 获取某一个标签内部的属性值attrs
# print(bs.a.attrs)
# #只获取某个标签的其中一个属性值
# print(bs.a["href"])
# print(bs.a.get("id"))
#获取标签的文本内容，string:获取某个标签的文本内容的时候，如果这个标签里面没有标签了，则.stirng获取的就是该标签的文本内容，如果该标签内容中还包括其他标签则返回None
# print(bs.title.string)
# print(type(bs.title.string))#NavigableString
# print(bs.div.string)
# print(bs.p.string)
# print(type(bs.p.string))#Comment


#------------------------文档树节点的选择--------------------------------------------------
#1>contents属性：遍历某一个父节点的直接子节点，可以将Tag类型的直接子节点以列表的方式进行输出，但是直接子节点内部的子节点是无法单独获取的。
print(bs.body.contents,'==============')
# #直接从子节点列表中获取某一个节点
# print(bs.body.contents[1])
# #2.>children属性，返回的是一个生成器对象，可以将Tag类型的直接子节点以生成器的方式进行输出，但是直接子节点的内部的子节点无法单独获取到。
# print(bs.body.children)
# for i,child in enumerate(bs.body.children):
#     print(i,child)

#3.>descendants属性：获取所有的子孙节点(即包含直接子节点，又包含子节点的子节点)，结果也是一个生成器对象
print(bs.body.descendants)
for i,child in enumerate(bs.body.descendants):
    print(i,child)
#4.>parent属性：获取父节点以及父节点包含的所有内容
print('====',bs.title.parent)

#5.>next_sibling属性:获取当前节点的下一个兄弟节点，如果没有下一个兄弟节点，则返回None
#实际文档中的tag的.next_sibiling和.previous_sibling属性通常是字符串或者空白，因为空白或者换行也可以被视作为一个节点，所以得到的结果可能是空白或者换行
# print("===",bs.meta.next_sibling)
# print("===",bs.meta.next_sibling.next_sibling)
#
# #6.>previous_sibling属性，获取当前节点的上一个兄弟节点，如果没有则返回None
# print("----",bs.title.previous_sibling)
# print("----",bs.title.previous_sibling.previous_sibling)


# -----------find_all()进行文档数内容的搜索------------
# 1.find_all()用于搜索当前节点的所有子节点，返回值是一个列表
# name, attrs, recursive, None,
# result_list = bs.find_all('a')
# print(result_list)
#
#
# result_list_1 = bs.find_all(attrs={"class":'second'})
# print(result_list_1)
# result_list_2 = bs.find_all(attrs={"id":"two"})
# print(result_list_2)

# 使用fian_all()方法时，BeautifulSoup会检索当前标签的所有子孙节点，如果只想搜索标签的直接子节点，可以将recursive设置为False,limit这个参数可以对找到的节点个数进行限制
# result_list_4 = bs.body.find_all(recursive=False,limit=2)
# print(result_list_4)
#
# result_list_5 = bs.find_all(text="淘宝")
# print(result_list_5)
#
# result_list_6 = bs.find_all(id="one")
# print(result_list_6)
#
# # 由于class是系统关键字，表示类，所以使用find_all来通过class属性值来匹配内容的时候，需要将class变为class_
# result_list_7 = bs.find_all(class_="second")
# print(result_list_7)
#
# result_list_8 = bs.find_all(id=re.compile("two"))
# print(result_list_8)


# find()和find_all()用法一致，只不过find_all()返回的是一个列表，find返回的是第一个符合条件的内容。
'''
（3）find_parents()  find_parent()

find_all() 和 find() 只搜索当前节点的所有子节点,孙子节点等. find_parents() 和 find_parent() 用来搜索当前节点的父辈节点,搜索方法与普通tag的搜索方法相同,搜索文档搜索文档包含的内容
（4）find_next_siblings()  find_next_sibling()

这2个方法通过 .next_siblings 属性对当 tag 的所有后面解析的兄弟 tag 节点进行迭代, find_next_siblings() 方法返回所有符合条件的后面的兄弟节点,find_next_sibling() 只返回符合条件的后面的第一个tag节点
（5）find_previous_siblings()  find_previous_sibling()

这2个方法通过 .previous_siblings 属性对当前 tag 的前面解析的兄弟 tag 节点进行迭代, find_previous_siblings() 方法返回所有符合条件的前面的兄弟节点, find_previous_sibling() 方法返回第一个符合条件的前面的兄弟节点
（6）find_all_next()  find_next()

这2个方法通过 .next_elements 属性对当前 tag 的之后的 tag 和字符串进行迭代, find_all_next() 方法返回所有符合条件的节点, find_next() 方法返回第一个符合条件的节点
（7）find_all_previous() 和 find_previous()

这2个方法通过 .previous_elements 属性对当前节点前面的 tag 和字符串进行迭代, find_all_previous() 方法返回所有符合条件的节点, find_previous()方法返回第一个符合条件的节点
'''

# ---------------通过css选择器进行文档数内容的搜索--
# 1.通过标签名来搜索一个标签
# print(bs.select("title"))
# print(bs.select("a"))
# # 2.通过class属性值来搜索一个标签
# # .是用来匹配一个属性值的固定用法
# print(bs.select(".second"))
# # 3.通过id这个属性值来搜索一个标签
# #    #是匹配id值的固定用法
# print(bs.select("#two"))
#
# # 4.组合查找
#
# print(bs.select("div #two"))
# print(bs.select("div .second"))
