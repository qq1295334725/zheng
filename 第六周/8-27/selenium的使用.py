"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:selenium.PY
@ide:PyCharm
@time:2018-08-27 10:04:30
"""
# selenium是一个网页自动化测试的一个工具，使用它可以操作浏览器来模拟人操作浏览器的行为。
# selenium：在爬虫中的使用。
# 1.获取动态的网页数据，一些动态的数据在网页的源代码中并没有显示，这时候可以考虑用selenium获取。
# 2.用于模拟登陆，对于一些需要登陆才能获取到数据的网页，一般如果采用分析参数破解的话，需要耗费大量的时间和精力进行网站的登录的破解，而如果使用selenium的话，就可以完全模拟人的登录行为来进行网站登录，就不需要分析参数进行网站的破解。


# selenium的特点：
# 1.它是通过驱动浏览器来进行网页的登录，或者是获取网页的信息。
# 2.由于selenium是驱动浏览器进行数据的爬取，而浏览器的打开，对网页发起请求，渲染页面都需要耗费大量的时间，所有一般不使用selenium进行网站数据的爬取，除非无法通过分析请求的方式进行网站登录，或者网站是动态网站，页面源代码中获取不到数据的这种情况下，才考虑使用selenium来进行爬取。
# 3.selenium提供的一些元素定位和查找的方法都是用纯python实现的，效率比较低。
# 4.selenium是免费开源的，支持很多的主流浏览器，IE，Chrome，Opera，FireFox，Safari等

# 1.安装selenium
# 2.安装浏览器驱动


from selenium import webdriver
# 第一步：创建一个浏览器对象
browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# 第二步：使用浏览器对象对网址发起请求
browser.get("https://www.baidu.com")
# 获取网页的源代码
print(browser.page_source)
# 获取此次请求的地址
print(browser.current_url)
# 获取此次请求的cookies信息
print(browser.get_cookies())
# 退出浏览器
browser.quit()






