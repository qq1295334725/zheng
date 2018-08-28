"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:selenium操作滚动条.PY
@ide:PyCharm
@time:2018-08-28 14:18:20
"""
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.cn")
driver.implicitly_wait(3)
driver.find_element_by_id("kw").send_keys("英雄联盟")
res = driver.find_element_by_partial_link_text("特玩游戏网").text
print(res)

# 方法一：将滚动条滚动到页面底部
# while True:
#     time.sleep(3)
#     js = "window.scrollTo(0, document.body.scrollHeight)"
#     # execute_script使用该方法来执行javascript语法
#     driver.execute_script(js)

# 方法二：将滚动条滚动到可视范围之内，只要能够定位到该元素即可，不适合AJXS请求


# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# driver.implicitly_wait(3)
# driver.find_element_by_id("kw").send_keys("英雄联盟")
# time.sleep(3)
# driver.find_element_by_id("su").click()
# time.sleep(3)
# target = driver.find_element_by_partial_link_text("特玩游戏网")
# driver.execute_script("arguments[0].scrollIntoView(false);",target)




