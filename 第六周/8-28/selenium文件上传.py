"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:selenium文件上传.PY
@ide:PyCharm
@time:2018-08-28 15:40:04
"""
# 通过selenium上传本地文件，一般先定位到网页中的上传按钮，通过send_keys()这个方法添加本地文件到网页中即可。
import os
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("C:/Users/Administrator/Desktop/正课/第六周/8-28/html/upload.html")
# 定位到上传按钮，添加本地文件
driver.find_element_by_xpath("//input[@value='上传']").send_keys("C:/Users/Administrator/Desktop/正课/第六周/8-28/text.text")


















