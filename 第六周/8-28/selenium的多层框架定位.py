"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:selenium的多层框架定位.PY
@ide:PyCharm
@time:2018-08-28 14:53:41
"""
# 对于一个web网站来说，有时候会遇到页面中含有内联框架iframe或者另一个window窗口。我们去定位框架或者窗口中的标签的时候，直接通过find_element_by_**这是方式无法直接定位到的，这时候必须要从外层窗口切换到内层窗口,然后再去定位。
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# file_path = "C:/Users/Administrator/Desktop/正课/html/frame.html"
file_path = "C:/Users/Administrator/Desktop/正课/第六周/8-28/html/frame.html"
driver.get(file_path)
# switch_to.frame(frame_reference)用来切换iframe框架的
# 参数frame_reference是用来定位iframe，可以传入ID，NAME等等
# 首先，切换到第一层frame
driver.switch_to.frame("f1")
# 接着，切换到第二层frame
time.sleep(3)
driver.switch_to.frame("f2")
time.sleep(3)
driver.find_element_by_partial_link_text("新闻").click()










