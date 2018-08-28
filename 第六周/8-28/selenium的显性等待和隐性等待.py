
"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:selenium的显性等待和隐性等待.PY
@ide:PyCharm
@time:2018-08-28 10:55:09
"""
# 一个网页在通过selenium驱动浏览器打开的时候，可能会由于网络慢，或者电脑卡顿，导致页面一时半会加载不完整，页面中的一些标签和样式还没有渲染出来。但是，代码执行速度很快，当通过使用代码定位元素的时候，可能回出现要查找的元素不存在的情况，代码会报异常。

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
browser = webdriver.Chrome()
browser.get("https://weibo.com/")
# time.sleep(10)
# time.sleep()可以让线程休眠一定的时间，等休眠时间到了之后，不管元素是否找到，rengranqiangzhixing往后执行。
# 一般这种方式不建议使用，会影响代码的实现效率，而且时间也不好把握。
# browser.find_element_by_link_text("动漫")

# 显性等待
# WebDriverWait这个类是用于设置显性等待的，经常配合着until使用，在页面加载期间，每隔一定的时间去查看元素是否被加载出来，如果没有加载出来，则继续等待，直到超出最大的等待时间，如果最后还是没有找到该元素，则最终抛出异常，如果在最大的时间范围内找到了该元素，则继续往后执行代码。
# a_element = WebDriverWait(browser,10).until(lambda browser:browser.find_element_by_link_text("动漫"))
# print(a_element)

# 隐性等待和time.sleep类似，设置一个最长等待时间，如果网页在规定的时候内加载完毕，则执行下一步，否则会一直处于等待状态，直到超时，一般一个程序内，只调用一次这样的方法即可。
browser.implicitly_wait(10)
a_element = browser.find_element_by_link_text("动漫")
print(a_element)


# 隐性等待implicitly_wait和显性等待WebDriverWait的区别：
# 1.隐性等待implicitly_wait是针对一整个页面，或者说是一个浏览器窗口而言，它是等待整个页面的元素被加载完成，而不是针对某一个元素，它是等到整个页面上的所有元素渲染完成之后，在进行查找和定位。
# 2.显性等待WebDriverWait是针对某一个元素而言，不是等待整个页面元素的渲染完成，而是等待某一个元素渲染完成，然后再去定位该元素，所以，每一个元素是否出现都可以使用显性等待来进行判断。

time.sleep(5)
browser.quit()











