"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:selenium操作cookie.PY
@ide:PyCharm
@time:2018-08-28 11:25:00
"""
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
print(browser.get_cookies())
cookie = [dict_test["name"]+"="+dict_test["value"] for dict_test in browser.get_cookies()]
cookie_str = ";".join(cookie)
with open("cookie.txt", 'w', encoding='utf-8') as f:
    f.write(cookie_str)




browser.quit()







