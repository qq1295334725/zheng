"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:sqlite3数据匹配.PY
@ide:PyCharm
@time:2018-08-02 14:11:09
"""
# like:主要用于匹配数据库中的多条记录
# 'a_':匹配以a开头，并且只匹配a后一个字符的数据。
# %a:匹配以a结尾的数据
# a%：匹配以a开头的数据
# %a%：匹配数据中包含a字符的数据。
import sqlite3
connect = sqlite3.connect('database.db')
cursor = connect.cursor()
# sql = "select * from teacher where name like '王_'"
# sql_1 = "select * from teacher where name like '%三'"
# sql_2 = "select * from teacher where name like '麻%'"
# sql_3 = "select * from teacher where name like '%五%'"
# res = cursor.execute(sql_3)
# for id,name,age,sex in res:
#     print(id,name,age,sex)

select_sql = 'select count(*) from teacher'
res = cursor.execute(select_sql)
count = res.fetchone()[0]
print(count)

connect.commit()
cursor.close()
connect.close()




















