"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:requests模块cookie信息自动追踪与管理.PY
@ide:PyCharm
@time:2018-08-15 10:46:10
"""
# requests这个模块，如果直接利用get（）或者post等方法可以做到模拟网页的请求，但是每一次请求之间是没有关系的，相当于不同的会话，也就是相当于用浏览器打开了两个不同的页面。
# 设想这样一个场景，第一层请求利用post（）方法登录了某个网站，第二次想获取成功登录之后的个人信息，又用了一次get（）方法去请求页面信息。实际上相当于打开了两个浏览器，是完全不相关的两个会话，这样不能成功获取个人信息。
# 解决方案：维持同一个会话，也就是相当于使用同一个浏览器打开不同的页面，而不是每次都要重新设置cookie，这时候就有了session对象
import requests
# 请求http://httpbin.org/cookies/set/number/123456789设置cookie信息，名称是number，内容是123456789，接着请求http://httpbin.org/cookies，这个网址可以获取当前的cookies
# requests.get("http://httpbin.org/cookies/set/number/123456789")
# r = requests.get("http://httpbin.org/cookies")
# print(r.text)

session_obj = requests.Session()
session_obj.get("http://httpbin.org/cookies/set/number/123456789")
r = session_obj.get("http://httpbin.org/cookies")
print(r.text)

















