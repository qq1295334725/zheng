"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:selenium的键盘事件.PY
@ide:PyCharm
@time:2018-08-27 16:15:01
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
# -------------------键盘操作事件-----------------
"""
send_keys():输入字符串
clear():清空文本框
send_keys(Keys.CONTROL,'a'):全选ctrl+a
send_keys(Keys.CONTROL,'x'):剪切ctrl+x
send_keys(Keys.CONTROL,'c'):复制ctrl+c
send_keys(Keys.CONTROL,'v'):粘贴ctrl+v
send_keys(Keys.ENTER):回车键：enter
send_keys(Keys.SPACE):空格键：Space
send_keys(Keys.BACK_SPACE):退格键：BACK_SPACE
send_keys(Keys.ESCAPE):退出键：Esc
send_keys(Keys.TAB):制表键：Tab
send_keys(Keys.SHIFT):上档键：Shift
send_keys(Keys.F1):键盘上的F1键
"""
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://sahitest.com/demo/label.htm")
time.sleep(3)
input1 = driver.find_element_by_xpath('//label[1]/input')
input2 = driver.find_element_by_xpath('//tr/td[2]/input')
input1.send_keys("张三")
time.sleep(3)
input1.send_keys(Keys.CONTROL,"a")
time.sleep(3)
input1.send_keys(Keys.CONTROL,"x")
time.sleep(3)
input2.send_keys(Keys.CONTROL,'v')
time.sleep(3)
input2.clear()

time.sleep(8)
driver.quit()












