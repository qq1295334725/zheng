"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:练习.PY
@ide:PyCharm
@time:2018-08-03 20:20:56
"""
# 练习：
# 1,创建一个学生成绩表 Grades，学号  姓名  成绩  名次
# CREATE TABLE Grades (num INTEGER PRIMARY KEY,name TEXT,grade INTEGER,rank INTEGER)
# 2，往表中插入10数据
# INSERT IN TO Grades (num,name,grade,rank) VALUES (1,’zhangsan’,398,20)
# 3，查询成绩大于60分的人的名字
# SELECT name,grade FROM grades WHERE grade > 60
# 4，查询成绩小于60分的人的个数
# SELECT COUNT(*) FROM grades WHERE grade < 60
# 5，把成绩小于60分的人的成绩修改为60分
# UPDATE grades SET grade = 60 WHERE grade < 60
# 6，删除所有学号小于100的人的信息
# DELETE FROM grades WHERE num < 100
# 6，查询姓“张”的人的所有信息
# SELECT * FROM grades WHERE name LIKE '张%'
# 7，查询所有人的成绩，按照成绩从高到低排列
# SELECT grade FROM grades ORDER BY grade DESC
# 8，查询所有人的成绩，按照名次从小到大排列
# SELECT grade FROM grades ORDER BY rank ASC

import sqlite3
connect = sqlite3.connect('Grades.db')
cursor = connect.cursor()
create_sql = "create table Grades(num INTEGER PRIMARY KEY,name TEXT,grade INTEGER,rank INTEGER)"
# cursor.execute(create_sql)
insert_sql = "insert into Grades(num,name,grade,rank)VALUES (6,'张飞',55,15)"
# cursor.execute(insert_sql)
select_sql = "select name,grade from Grades WHERE grade>60"
# result = cursor.execute(select_sql)
# for name,grade in result:
#     print('及格的学生：',name,'-',grade)

select1_sql = "select count(*) from Grades WHERE grade<60"
# result1 = cursor.execute(select1_sql)
# res = result1.fetchone()
# print('不及格的人数为：',res)

update_sql = "update Grades set grade=%d WHERE grade<60"%(60)
# cursor.execute(update_sql)

delete_sql = "delete from Grades WHERE num<3"
cursor.execute(delete_sql)

select2_sql = "select * from Grades WHERE name like '张%'"
# for num,name,grade,rank in cursor.execute(select2_sql):
#     print(num,'.',name,grade,rank)

select3_sql = "select grade from Grades order by grade desc"
# res = cursor.execute(select3_sql)
# print(res)
# for grade in res:
#     print(grade,end=' ')

select4_sql = "select grade from Grades order by rank asc"
res1 = cursor.execute(select4_sql)
for grade in res1:
    print(grade,end=' ')

connect.commit()
cursor.close()
connect.close()













