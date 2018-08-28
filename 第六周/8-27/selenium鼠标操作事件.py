"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:selenium鼠标操作事件.PY
@ide:PyCharm
@time:2018-08-27 14:56:28
"""
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

# ------------------鼠标点击事件---------------
# click():单机鼠标左键
# 2.double_click():鼠标左键双击
# 3.context_click():鼠标右键单击
# 4.click_and_hold():点击鼠标左键，不松开
# release():松开鼠标左键
browser = webdriver.Chrome()
# browser.maximize_window()
browser.get("http://www.sahitest.com/demo/clicks.htm")
time.sleep(3)
# # 定义一个ActionChains类的对象，参数是浏览器对象
# # ActionChains类，需要一个参数：浏览器对象，当调用相关鼠标操作函数的时候，这些事件并不会立刻执行，而是将所有的鼠标事件都放入到一个队列当中，只有执行perform函数的时候，所有的鼠标事件才会被执行。
action = ActionChains(browser)
click_me = browser.find_element_by_xpath('//input[@value="click me"]')
double_click = browser.find_element_by_xpath('//input[@value="dbl click me"]')
right_click = browser.find_element_by_xpath('//input[@value="right click me"]')
action.click(click_me)
action.double_click(double_click)
action.context_click(right_click)
action.perform()

# ---------------鼠标移动事件--------------------
# move_to_element():鼠标移动至摸个元素
# move_by_offset(x,y):鼠标移动到当前位置的某个坐标
# move_to_element_with_offset(element,x,y):移动到距离某个元素（多少距离）的位置
# browser = webdriver.Chrome()
# # browser.maximize_window()
# browser.get("http://sahitest.com/demo/mouseover.htm")
# time.sleep(3)
# action = ActionChains(browser)
# # move_element = browser.find_element_by_xpath("//input[@value='Write on hover']")
# move_element = browser.find_element_by_xpath("//a[@href='x']//span")
# action.move_to_element(move_element)
# action.perform()


# ----------鼠标拖拽事件-----------------------
# drag_and_drop():拖拽到某个元素然后松开
# drap_and_drop_by_offset(source,x,y):拖拽到距离某个坐标点多少的位置然后松开

browser = webdriver.Chrome()
# browser.maximize_window()
browser.get("http://sahitest.com/demo/dragDropMooTools.htm")
time.sleep(3)
# 首先找到被拖拽元素
dragger = browser.find_element_by_id("dragger")
# 找到要被拖拽到的元素位置
target1 = browser.find_element_by_xpath('//div[text()="Item 1"]')
target2 = browser.find_element_by_xpath('//div[text()="Item 2"]')
target3 = browser.find_element_by_xpath('//div[text()="Item 3"]')
target4 = browser.find_element_by_xpath('//div[text()="Item 4"]')
action = ActionChains(browser)
# 方式一：
# action.drag_and_drop(dragger, target1)
# time.sleep(2)
# action.perform()
# action.drag_and_drop(dragger, target2)
# time.sleep(2)
# action.perform()
# action.drag_and_drop(dragger, target3)
# time.sleep(2)
# action.perform()
# action.drag_and_drop(dragger, target4)

# action.drag_and_drop(browser.find_element_by_id("dragger"),browser.find_element_by_xpath('//div[text()="Item 1"]'))
# 方式二：
# action.click_and_hold(dragger).move_to_element(target1).release()
# 方式三：
action.click_and_hold(dragger).release(target1)
action.perform()
time.sleep(10)
browser.quit()









