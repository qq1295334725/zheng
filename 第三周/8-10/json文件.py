"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:json文件.PY
@ide:PyCharm
@time:2018-08-10 10:27:30
"""
import json
f = open('泛见志.txt','r',encoding='utf-8')
res = json.loads(f.read())
print(res)