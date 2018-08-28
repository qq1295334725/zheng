"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:selenium的浏览器操作事件.PY
@ide:PyCharm
@time:2018-08-27 11:38:47
"""
# 1.maximize_window()可以使窗口最大化
# 2.minimize_window()使窗口最小化
# 3.set_window_size()设置浏览器的窗口大小（第一个参数宽，第二个参数高）
# 4.back():浏览器前进
# 5.forward():浏览器后退
# 6.refresh（）：浏览器刷新
# 7.current_window_handle:浏览器当前选项卡（浏览器窗口）
# 8.window_handle:浏览器打开的所有选项卡（浏览器窗口）
# 9.switch_to.window:切换浏览器选项卡（切换浏览器窗口）
# 10.clise():关闭当前浏览器选项卡（浏览器窗口）
# 11.quit（）：关闭浏览器
import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()
browser.minimize_window()
browser.set_window_size(480,800)
browser.get("https://www.baidu.com")
time.sleep(3)
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.back()
time.sleep(2)
browser.refresh()
time.sleep(2)
browser.forward()



browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.baidu.com")
print(browser.current_window_handle)
time.sleep(3)
browser.find_element_by_id("kw").send_keys("英雄联盟")
browser.find_element_by_id("su").click()
print(browser.current_window_handle)
time.sleep(3)
browser.find_element_by_partial_link_text("泳池派对").click()
print(browser.current_window_handle)
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
time.sleep(3)
# browser.close()
browser.quit()










