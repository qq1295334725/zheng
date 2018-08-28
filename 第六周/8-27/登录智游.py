"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:登录智游.PY
@ide:PyCharm
@time:2018-08-27 16:40:29
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get("http://kaoshi.zhiyou900.com:8888/edustu/login/login.spr")

time.sleep(3)
input1 = driver.find_element_by_xpath('//input[@name="j_username"]').send_keys("13525517200")
input2 = driver.find_element_by_xpath('//input[@name="j_password"]').send_keys("123456")
button = driver.find_element_by_xpath('//button[@type="submit"]').click()
print(driver.get_cookies())


















