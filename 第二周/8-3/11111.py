"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:11111.PY
@ide:PyCharm
@time:2018-08-04 16:22:44
"""
import sqlite3
# 新建表的函数
def create_table_student():
    connect = sqlite3.connect('student.db')
    cursor = connect.cursor()
    create_table = "create table stu(id INTEGER PRIMARY KEY,name TEXT,age INTEGER,score INTEGER)"
    table = cursor.execute(create_table)
    return table
# 查询学生总数的函数
def select_count():
    select_count_sql = "select count(*) from table"

    count = cursor.execute(select_count_sql)











