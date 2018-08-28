"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:selenium元素定位及标签文本和属性值的获取.PY
@ide:PyCharm
@time:2018-08-27 10:58:50
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")

# --------------------定位单个节点--------
# # 通过id值匹配
# res1 = browser.find_element_by_id("kw")
# print(res1)
# # 通过name值匹配
# res2 = browser.find_element_by_name("wd")
# print(res2)
# # 通过class属性值匹配
# res3 = browser.find_element_by_class_name("s_ipt")
# print(res3)
# # 通过css选择器来匹配
# res4 = browser.find_element_by_css_selector("#kw")
# print(res4)
# # 通过xpath进行匹配
# res5 = browser.find_element_by_xpath("//input[@id='kw']")
# print(res5)
# # 通过标签名进行匹配
# res6 = browser.find_element_by_tag_name("input")
# print(res6)
# # 通过文本链接匹配
# res7 = browser.find_element_by_link_text("新闻")
# print(res7)
# # 针对一些比较长的文本链接，取其中的一小部分文本值进行匹配
# res8 = browser.find_element_by_partial_link_text("贴")
# print(res8)
# browser.quit()


# -------------定位到多个节点------------------
# # 通过id值匹配
# res1 = browser.find_elements_by_id("kw")
# print(res1)
# # 通过name值匹配
# res2 = browser.find_elements_by_name("wd")
# print(res2)
# # 通过class属性值匹配
# res3 = browser.find_elements_by_class_name("s_ipt")
# print(res3)
# # 通过css选择器来匹配
# res4 = browser.find_elements_by_css_selector("#kw")
# print(res4)
# # 通过xpath进行匹配
# res5 = browser.find_elements_by_xpath("//input[@id='kw']")
# print(res5)
# # 通过标签名进行匹配
# res6 = browser.find_elements_by_tag_name("input")
# print(res6)
# # 通过文本链接匹配
# res7 = browser.find_elements_by_link_text("新闻")
# print(res7)
# # 针对一些比较长的文本链接，取其中的一小部分文本值进行匹配
# res8 = browser.find_elements_by_partial_link_text("贴")
# print(res8)
# browser.quit()

# -------------通用方法------------------
# find_element():一次只能查找一个element对象，第一个参数：设置要查找的方式：第二个参数：设置要查找的值
# find_elements():一次能查找多个element对象，第一个参数：设置要查找的方式：第二个参数：设置要查找的值
# res1 = browser.find_elements(By.ID,"kw")
# print(res1)
# res2 = browser.find_elements(By.NAME,"wd")
# print(res2)
# res3 = browser.find_elements(By.CLASS_NAME,"s_ipt")
# print(res3)
# res4 = browser.find_elements(By.CSS_SELECTOR,"#kw")
# print(res4)
# res5 = browser.find_elements(By.XPATH,"//input[@id='kw']")
# print(res5)
# res6 = browser.find_elements(By.TAG_NAME,"input")
# print(res6)
# res7 = browser.find_elements(By.LINK_TEXT,"新闻")
# print(res7)
# res8 = browser.find_elements(By.PARTIAL_LINK_TEXT,"贴")
# print(res8)
# browser.quit()


# -----------获取标签的属性值和文本------------
attriubute = browser.find_element_by_name("tj_trnews").get_attribute("href")
print(attriubute)
text = browser.find_element_by_name("tj_trnews").text
print(text)
a_list = browser.find_elements_by_class_name("mnav")
print(a_list)
for a in a_list:
    print(a.get_attribute("href"))
    print(a.text)


browser.quit()
