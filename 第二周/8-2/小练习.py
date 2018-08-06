"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:小练习.PY
@ide:PyCharm
@time:2018-08-02 11:17:31
"""
# 小练习：
# 1.创建一个数据库teacher
# 2.创建一个表tea，字段（id(主键)，name，age，sex）
# 3.往tea表中插入数据（张三，20，男）
# 4.往tea表中插入数据（李四，30，女）
# 5.修改（李四，30，女）这条数据，改为（王五，22，男）
# 6.删除（张三，男，20）这条数据
# 7.将表中所有的数据查询出来
import sqlite3
connect = sqlite3.connect('teacher.db')
cursor = connect.cursor()
creat_sql = "creat table tea(i"




















