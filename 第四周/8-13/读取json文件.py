"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:读取json文件.PY
@ide:PyCharm
@time:2018-08-13 11:31:25
"""
import json
f = open('pengpai.txt','r',encoding='utf-8')
res = json.loads(f.read())
for dict_test in res:
    print(dict_test["新闻标题"])
